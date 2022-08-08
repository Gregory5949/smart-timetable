import json
import logging
from datetime import date, datetime
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from db import Database
from models import EventRealization, Role
from timetable_builder import TimetableBuilder


class TimetableStorage:
    def __init__(self, db: Database) -> None:
        self._built_timetable: dict[str, EventRealization] = {}
        self._db = db
        self._builder = TimetableBuilder(db)

    def reload(self) -> None:
        logging.info("Building random timetable...")
        self._built_timetable = self._builder.build_fixed()
        logging.info("Random timetable built")

    def get_timetable(self, person_id: str, start: date, end: date) -> list[Any]:
        return [
            {
                "id": ea.event_id,
                "lesson": {
                    "subject": {
                        "id": (cuid := (ev := self._db.get_event(ea.event_id)).course_unit_id),
                        "name": (cu := self._db.get_course_unit(cuid)).name,
                        "name_short": cu.name_short,
                    },
                    "name": ev.name,
                    "name_short": ev.name,
                    "description": None,
                    "type": ev.type.value,
                    "format": None,
                },
                "start": datetime.combine(
                    (er := self._built_timetable[ea.event_id]).date,
                    (gs := self._db.get_grid_slot(er.grid_slot_id)).starts_at,
                ),
                "end": datetime.combine(er.date, gs.ends_at),
                "location": {
                    "full": f"{self._db.get_building((r := self._db.get_room(er.room_id)).building_id).name} {r.name}",
                },
                "teachers": [
                    {
                        "id": p.person_id,
                        "first_name": "Abstract Teacher",
                        "last_name": p.person_id,
                        "full_name": p.person_id,
                    }
                    for p in self._db.get_event_attendees_by_event(ea.event_id)
                    if p.role == Role.TEACH
                ] or [
                    {
                        "id": person_id,
                        "first_name": "No Teacher",
                        "last_name": "ALERT",
                        "full_name": "No Teacher",
                    }
                ],
                "team_name": None,
            }
            # for ea in self._db.get_event_attendees_by_person(person_id)
            for ea in self._db.event_attendees
            if (
                ea.event_id in self._built_timetable
                and start <= self._built_timetable[ea.event_id].date <= end
            )
        ]

    def get_people(self, query: str) -> list[Any]:
        return [
            {
                "id": p,
                "first_name": f"Abstract User",
                "last_name": f"{p}",
                "full_name": f"{p}",
            }
            for p in set(
                ea.person_id
                for ea in self._db.event_attendees
                if query in ea.person_id
            )
        ][:25]


logging.basicConfig(level=logging.INFO)

app = FastAPI()
database = Database()
store = TimetableStorage(database)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/search")
def search(person_name: str):
    return store.get_people(person_name)


@app.get("/person/{uuid}")
def get_person(uuid: str):
    return {
        "id": uuid,
        "first_name": f"Abstract User",
        "last_name": f"{uuid}",
        "full_name": f"{uuid}",
    }


@app.get("/event/{event_id}/team")
def get_team(event_id: str):
    return [
        get_person(ea.person_id)
        for ea in database.get_event_attendees_by_event(event_id)
    ]


@app.get("/person/{uuid}/timetable")
def get_timetable(uuid: str, to: datetime, from_: datetime = Query(alias="from")):
    print(uuid, to, from_)
    return store.get_timetable(uuid, from_.date(), to.date())


@app.get("/timetabled-users")
def get_timetabled_user_ids():
    return set(
        ea.person_id
        for ea in database.event_attendees
        if ea.event_id in store._built_timetable
    )


class JSONReprResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            separators=(",", ":"),
            default=repr,
        ).encode("utf-8")


@app.get("/dump-timetable")
def dump_timetable():
    return JSONReprResponse(store._built_timetable)


@app.get("/reload")
def reload():
    logging.warning("Reloading timetable")
    store.reload()
    return {"status": "ok"}


@app.on_event("startup")
def on_startup():
    database.load_from_dir(Path("modeus-data"))
    store.reload()

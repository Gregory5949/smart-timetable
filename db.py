from __future__ import annotations

import functools
import logging
from csv import reader
from datetime import date, datetime, timedelta
from os import PathLike
from pathlib import Path
from typing import Any, Callable, Iterable, ParamSpec, TypeVar

from models import (
    Building, BuildingDistance, CourseUnit, CycleRealization, Event, EventAttendee,
    EventType, Grid, GridSlot, Role, Room, RoomType, Schedule,
)

_DATEFMT = "%Y-%m-%d %H:%M:%S.%f"
_TIMEFMT = "%H:%M:%S"

_PS = ParamSpec("_PS")
_RT = TypeVar("_RT")


def _read(filename: str | PathLike[str]) -> Iterable[dict[str, str]]:
    with open(filename, "r") as f:
        rd = reader(f)
        keys = next(rd)  # header
        for row in rd:
            yield dict(zip(keys, row))


def _parse_duration(value: int, unit: str) -> timedelta:
    match unit:
        case "ACADEMIC_HOUR":
            mul = 45
        case "PAIR":
            mul = 90
        case "MINUTE":
            mul = 1
        case _:
            raise ValueError(f"Unknown duration unit: {unit}")
    return timedelta(minutes=mul * value)


def _ensure_loaded(f: Callable[_PS, _RT]) -> Callable[_PS, _RT]:
    @functools.wraps(f)
    def wrapper(self: Database, *args: _PS.args, **kwargs: _PS.kwargs) -> _RT:
        if not self._is_loaded:
            raise RuntimeError("Database is not loaded. Use load_from_dir() first.")
        return f(self, *args, **kwargs)
    return wrapper


class Database:
    """Represents entire database."""

    def __init__(self):
        self._buildings: dict[str, Building] = {}
        self._building_distances: dict[tuple[str, str], BuildingDistance] = {}
        self._course_units: dict[str, CourseUnit] = {}
        self._cycle_realizations: dict[str, CycleRealization] = {}
        self._day_offs: set[date] = set()
        self._events: dict[str, Event] = {}
        self._event_attendees: dict[tuple[str, str], EventAttendee] = {}
        self._grids: dict[str, Grid] = {}
        self._grid_slots: dict[str, GridSlot] = {}
        self._schedules: dict[str, Schedule] = {}
        self._rooms: dict[str, Room] = {}
        self._room_types: dict[str, RoomType] = {}
        self._is_loaded = False

    def load_from_dir(self, directory: Path) -> None:
        """Loads database from directory."""

        if not directory.is_dir():
            raise ValueError(f"{directory} is not a directory")

        logging.info(f"Loading data from {directory.resolve()}...")

        self._buildings = {
            b["id"]: Building(
                id=b["id"],
                name=b["name"],
                name_short=b["name_short"],
            )
            for b in _read(directory / "building.csv")
        }
        self._building_distances = {
            (bd["from_building_id"], bd["to_building_id"]): BuildingDistance(
                from_building_id=bd["from_building_id"],
                to_building_id=bd["to_building_id"],
                duration=_parse_duration(int(bd["duration_value"]), bd["duration_unit_id"]),
            )
            for bd in _read(directory / "building_distance.csv")
        }
        self._course_units = {
            cu["id"]: CourseUnit(
                id=cu["id"],
                name=cu["name"],
                name_short=cu["name_short"],
                starts_at=datetime.strptime(cu["starts_at_lt"], _DATEFMT),
                ends_at=datetime.strptime(cu["ends_at_lt"], _DATEFMT),
            )
            for cu in _read(directory / "course_unit.csv")
        }
        self._cycle_realizations = {
            cr["id"]: CycleRealization(
                id=cr["id"],
                code=cr["code"],
                course_unit_id=cr["course_unit_id"],
            )
            for cr in _read(directory / "cycle_realization.csv")
        }
        self._day_offs = set(
            datetime.strptime(do["date"], _DATEFMT).date()
            for do in _read(directory / "academic_calendar_irregular_rule.csv")
        ),
        self._events = {
            e["id"]: Event(
                id=e["id"],
                course_unit_id=e["course_unit_id"],
                cycle_realization_id=e["cycle_realization_id"],
                ordinal=int(e["ordinal"]),
                schedule_id=e["schedule_id"],
                type=EventType(e["type_id"]),
                name=e["name"],
                duration=_parse_duration(
                    int(e["duration_value"]), e["duration_unit_id"]
                ),
                capacity_required=int(e["capacity_required"]),
            )
            for e in _read(directory / "event.csv")
        }
        self._event_attendees = {
            (ea["event_id"], ea["person_id"]): EventAttendee(
                event_id=ea["event_id"],
                role=Role(ea["role_id"]),
                person_id=ea["person_id"],
            )
            for ea in _read(directory / "event_attendee.csv")
        }
        self._grids = {
            g["id"]: Grid(
                id=g["id"],
                name=g["name"],
            )
            for g in _read(directory / "grid.csv")
        }
        self._grid_slots = {
            gs["id"]: GridSlot(
                id=gs["id"],
                grid_id=gs["grid_id"],
                name=gs["name"],
                starts_at=datetime.strptime(gs["starts_at_lt"], _TIMEFMT).time(),
                ends_at=datetime.strptime(gs["ends_at_lt"], _TIMEFMT).time(),
            )
            for gs in _read(directory / "grid_slot.csv")
        }
        self._schedules = {
            s["id"]: Schedule(
                id=s["id"],
                name=s["name"],
                starts_at=datetime.strptime(s["starts_at_lt"], _DATEFMT),
                ends_at=datetime.strptime(s["ends_at_lt"], _DATEFMT),
            )
            for s in _read(directory / "schedule.csv")
        }
        self._rooms = {
            r["id"]: Room(
                id=r["id"],
                building_id=r["building_id"],
                name=r["name"],
                name_short=r["name_short"],
                type_id=r["type_id"],
                working_capacity=int(r["working_capacity"]),
                total_capacity=int(r["total_capacity"]),
            )
            for r in _read(directory / "room.csv")
        }
        self._room_types = {
            rt["id"]: RoomType(
                id=rt["id"],
                name=rt["name"],
            )
            for rt in _read(directory / "room_type.csv")
        }
        self._is_loaded = True

        logging.info("Data loaded")

    # @_ensure_loaded
    def get_building(self, building_id: str) -> Building:
        """Returns building with given ID."""
        return self._buildings[building_id]

    @property
    # @_ensure_loaded
    def buildings(self) -> list[Building]:
        """Returns list of all buildings."""
        return list(self._buildings.values())

    # @_ensure_loaded
    def get_building_distance(self, from_building_id: str, to_building_id: str) -> BuildingDistance:
        """Returns building distance between two buildings."""
        return self._building_distances[(from_building_id, to_building_id)]

    @property
    # @_ensure_loaded
    def building_distances(self) -> list[BuildingDistance]:
        """Returns list of all building distances."""
        return list(self._building_distances.values())

    # @_ensure_loaded
    def get_course_unit(self, course_unit_id: str) -> CourseUnit:
        """Returns course unit with given ID."""
        return self._course_units[course_unit_id]

    @property
    # @_ensure_loaded
    def course_units(self) -> list[CourseUnit]:
        """Returns list of all course units."""
        return list(self._course_units.values())

    # @_ensure_loaded
    def get_cycle_realization(self, cycle_realization_id: str) -> CycleRealization:
        """Returns cycle realization with given ID."""
        return self._cycle_realizations[cycle_realization_id]

    @property
    # @_ensure_loaded
    def cycle_realizations(self) -> list[CycleRealization]:
        """Returns list of all cycle realizations."""
        return list(self._cycle_realizations.values())

    # @_ensure_loaded
    def is_day_off(self, day: date) -> bool:
        """Returns True if given day is a day off."""
        return day in self._day_offs

    @property
    # @_ensure_loaded
    def day_offs(self) -> list[date]:
        """Returns list of all day offs."""
        return list(self._day_offs)

    # @_ensure_loaded
    def get_event(self, event_id: str) -> Event:
        """Returns event with given ID."""
        return self._events[event_id]

    @property
    # @_ensure_loaded
    def events(self) -> list[Event]:
        """Returns list of all events."""
        return list(self._events.values())

    # @_ensure_loaded
    def get_event_attendee(self, event_id: str, person_id: str) -> EventAttendee:
        """Returns event attendee with given event ID and person ID."""
        return self._event_attendees[(event_id, person_id)]

    # @_ensure_loaded
    def get_event_attendees_by_event(self, event_id: str) -> list[EventAttendee]:
        """Returns list of event attendees for given event ID."""
        return [
            ea
            for ea in self._event_attendees.values()
            if ea.event_id == event_id
        ]

    # @_ensure_loaded
    def get_event_attendees_by_person(self, person_id: str) -> list[EventAttendee]:
        """Returns list of event attendees for given person ID."""
        return [
            ea
            for ea in self._event_attendees.values()
            if ea.person_id == person_id
        ]

    @property
    # @_ensure_loaded
    def event_attendees(self) -> list[EventAttendee]:
        """Returns list of all event attendees."""
        return list(self._event_attendees.values())

    # @_ensure_loaded
    def get_grid(self, grid_id: str) -> Grid:
        """Returns grid with given ID."""
        return self._grids[grid_id]

    @property
    # @_ensure_loaded
    def grids(self) -> list[Grid]:
        """Returns list of all grids."""
        return list(self._grids.values())

    # @_ensure_loaded
    def get_grid_slot(self, grid_slot_id: str) -> GridSlot:
        """Returns grid slot with given ID."""
        return self._grid_slots[grid_slot_id]

    @property
    # @_ensure_loaded
    def grid_slots(self) -> list[GridSlot]:
        """Returns list of all grid slots."""
        return list(self._grid_slots.values())

    # @_ensure_loaded
    def get_schedule(self, schedule_id: str) -> Schedule:
        """Returns schedule with given ID."""
        return self._schedules[schedule_id]

    @property
    # @_ensure_loaded
    def schedules(self) -> list[Schedule]:
        """Returns list of all schedules."""
        return list(self._schedules.values())

    @_ensure_loaded
    def get_room(self, room_id: str) -> Room:
        """Returns room with given ID."""
        return self._rooms[room_id]

    @property
    # @_ensure_loaded
    def rooms(self) -> list[Room]:
        """Returns list of all rooms."""
        return list(self._rooms.values())

    # @_ensure_loaded
    def get_room_type(self, room_type_id: str) -> RoomType:
        """Returns room type with given ID."""
        return self._room_types[room_type_id]

    @property
    # @_ensure_loaded
    def room_types(self) -> list[RoomType]:
        """Returns list of all room types."""
        return list(self._room_types.values())

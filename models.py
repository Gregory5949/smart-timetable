from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from enum import Enum, auto
from typing import Protocol, TypeVar


class _AutoNameEnum(Enum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_value: list[str]) -> str:
        return name


class HasID(Protocol):
    id: str


_T = TypeVar("_T", bound=HasID)


def _magic_getter(items: list[_T], target_id: str) -> _T:
    for item in items:
        if item.id == target_id:
            return item
    raise ValueError("No associated item found")


# PyCharm argues about invalid `auto` call.
# noinspection PyArgumentList
class EventType(_AutoNameEnum):
    MID_CHECK = auto()
    SEMI = auto()
    LECT = auto()
    CONS = auto()
    LAB = auto()
    CUR_CHECK = auto()
    SELF = auto()


@dataclass()
class CourseUnit(HasID):
    id: str
    name: str
    name_short: str
    starts_at: datetime
    ends_at: datetime


@dataclass()
class CycleRealization(HasID):
    id: str
    code: str
    course_unit_id: str

    def get_course_unit(self, course_units: list[CourseUnit]) -> CourseUnit:
        return _magic_getter(course_units, self.course_unit_id)


@dataclass()
class Schedule(HasID):
    id: str
    name: str
    starts_at: datetime
    ends_at: datetime


@dataclass()
class Event(HasID):
    id: str
    course_unit_id: str
    cycle_realization_id: str
    ordinal: int
    schedule_id: str
    type: EventType
    name: str
    duration: timedelta
    capacity_required: int

    def get_course_unit(self, course_units: list[CourseUnit]) -> CourseUnit:
        return _magic_getter(course_units, self.course_unit_id)

    def get_cycle_realization(self, cycle_realizations: list[CycleRealization]) -> CycleRealization:
        return _magic_getter(cycle_realizations, self.cycle_realization_id)

    def get_schedule(self, schedules: list[Schedule]) -> Schedule:
        return _magic_getter(schedules, self.schedule_id)


# noinspection PyArgumentList
class Role(_AutoNameEnum):
    STUDENT = auto()
    TEACH = auto()
    TECH_WORKER = auto()
    MODER = auto()
    ASSISTANT = auto()


@dataclass()
class EventAttendee:
    event_id: str
    role: Role
    person_id: str

    def get_event(self, events: list[Event]) -> Event:
        return _magic_getter(events, self.event_id)


@dataclass()
class Grid(HasID):
    id: str
    name: str


@dataclass()
class GridSlot(HasID):
    id: str
    grid_id: str
    name: str
    starts_at: datetime
    ends_at: datetime

    def get_grid(self, grids: list[Grid]) -> Grid:
        return _magic_getter(grids, self.grid_id)


@dataclass()
class Building(HasID):
    id: str
    name: str
    name_short: str


@dataclass()
class RoomType(HasID):
    id: str
    name: str


@dataclass()
class Room(HasID):
    id: str
    building_id: str
    name: str
    name_short: str
    type_id: str
    working_capacity: int
    total_capacity: int

    @property
    def effective_capacity(self) -> int:
        return min(self.working_capacity, self.total_capacity)

    def get_building(self, buildings: list[Building]) -> Building:
        return _magic_getter(buildings, self.building_id)

    def get_room_type(self, room_types: list[RoomType]) -> RoomType:
        return _magic_getter(room_types, self.type_id)


@dataclass()
class GridSlot(HasID):
    id: str
    grid_id: str
    name: str
    starts_at: time
    ends_at: time

    def get_grid(self, grids: list[Grid]) -> Grid:
        return _magic_getter(grids, self.grid_id)


@dataclass()
class EventRealization:
    event_id: str
    room_id: str
    grid_slot_id: str
    date: date

    def get_event(self, events: list[Event]) -> Event:
        return _magic_getter(events, self.event_id)

    def get_room(self, rooms: list[Room]) -> Room:
        return _magic_getter(rooms, self.room_id)

    def get_grid_slot(self, grid_slots: list[GridSlot]) -> GridSlot:
        return _magic_getter(grid_slots, self.grid_slot_id)


@dataclass()
class BuildingDistance:
    from_building_id: str
    to_building_id: str
    duration: timedelta

    @property
    def is_transport_required(self) -> bool:
        return self.duration > timedelta(minutes=10)

    def get_from_building(self, buildings: list[Building]) -> Building:
        return _magic_getter(buildings, self.from_building_id)

    def get_to_building(self, buildings: list[Building]) -> Building:
        return _magic_getter(buildings, self.to_building_id)

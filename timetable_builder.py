import datetime
import random
import math
from collections import Counter

from db import Database
from models import (
    EventRealization, Room
)

def peak_room(needed_capacity: int, rooms: list[Room], prec: int) -> Room:
    left, right = 0, len(rooms) - 1
    while left <= right:
        mid = (left + right) // 2
        if all(rooms[mid].effective_capacity - i < needed_capacity for i in range(prec + 1)):
            left = mid + 1
        elif all(rooms[mid].effective_capacity - i > needed_capacity for i in range(prec + 1)):
            right = mid - 1
        else:
            return rooms[mid]


def calculate_fitness(data: Database, timetable: dict[str, EventRealization]) -> float:
    classes = list(timetable.values())
    conflicts: Counter[str, int] = Counter()
    for i in range(len(classes)):
        for j in range(i + 1, len(classes)):
            if classes[i].date == classes[j]:
                if classes[i].grid_slot_id == classes[j].grid_slot_id:
                    conflicts["time_con"] += 1

        if data.get_room(classes[i].room_id).effective_capacity < len(
                data.get_event_attendees_by_event(classes[i].event_id)
        ):
            conflicts["capacity_con"] += 1

    return 1 / (1 + sum(conflicts.values()))


def selection(data: Database, population: list[(dict[str, EventRealization])]) -> list[
    (dict[str, EventRealization])]:
    fitness : list[float] = []
    fittest: list[(dict[str, EventRealization], float)] = []
    for i in population:
        fitness.append(calculate_fitness(data, i))
    tmp_max = 0
    tmp_ttb = 0
    for i, j in zip(population, fitness):
        if j > tmp_max:
            tmp_max = j
            tmp_ttb = i
    fittest.append((tmp_ttb, tmp_max))
    # for i, j in zip(population, fitness):
    #     if 0 < j < tmp_max:
    #         tmp_max = j
    #         tmp_ttb = i
    # fittest.append((tmp_ttb, tmp_max))
    return fittest


class TimetableBuilder:
    def __init__(
            self,
            data: Database,
    ):
        self._data = data

    def _get_working_days(self) -> list[datetime]:
        working_days: list[datetime] = []
        start = datetime.datetime(2022, 2, 6)
        end = datetime.datetime(2022, 7, 10)
        delta = end - start
        for i in range(delta.days + 1):
            day = start + datetime.timedelta(days=i)
            if day.date() not in self._data.day_offs and day.weekday() != 6:
                working_days.append(day.date())
        return working_days

    def build_random(self) -> dict[str, EventRealization]:
        """Builds random timetable. Returns a map of `event_id` to `EventRealization`."""
        grid_ids: list[str] = [
            "Grid.05.01",
            "Grid.05.02",
            "Grid.05.03",
            "Grid.05.04",
            "Grid.05.05",
            "Grid.05.06",
            "Grid.05.07",
            "Grid.05.08"
        ]
        grid_slots_uni = [grid_slot for grid_slot in self._data.grid_slots if
                          grid_slot.id in grid_ids]
        working_days = self._get_working_days()
        timetable: dict[str, EventRealization] = {}
        rooms_sorted = sorted(self._data.rooms, key=lambda x: x.effective_capacity)
        for day in working_days:
            slots = random.choices(grid_slots_uni, k=random.randint(2, 5))
            rooms = []
            events = random.choices([event for event in self._data.events if event.capacity_required < 301],
                                    k=len(slots))
            for event in events:
                peaked = peak_room(event.capacity_required, rooms_sorted, math.ceil(event.capacity_required * 0.46))
                rooms.append(peaked)

            for event, room, slot in zip(events, rooms, slots):
                timetable.setdefault(
                    event.id, EventRealization(event.id, room.id, slot.id, day)
                )
        return timetable

    def build_optimized(self) -> dict[str, EventRealization]:
        """Builds optimized timetable. Returns a map of `event_id` to `EventRealization`."""
        raise NotImplementedError

    def build_fixed(self) -> dict[str, EventRealization]:
        """Returns a fixed optimal map of `event_id` to `EventRealization`."""
        return {
            '359711a5-34da-4f4a-a2a4-cb10a1db6084': EventRealization(
                event_id='359711a5-34da-4f4a-a2a4-cb10a1db6084',
                room_id='1bf7559f-f5d0-4f81-9bd0-a5fa9e889b0e', grid_slot_id='Grid.05.06',
                date=datetime.date(2022, 2, 7)
            ), '2234332d-fa4a-40c9-b09b-d231c7e524af': EventRealization(
                event_id='2234332d-fa4a-40c9-b09b-d231c7e524af',
                room_id='39ed6f07-80da-4759-910e-9ba4286bd0a3', grid_slot_id='Grid.05.08',
                date=datetime.date(2022, 2, 7)
            ), '1682d60b-ae6f-41d4-809c-aa550f4209f0': EventRealization(
                event_id='1682d60b-ae6f-41d4-809c-aa550f4209f0',
                room_id='6c27980e-5566-47de-ad09-cc04d96552d5', grid_slot_id='Grid.05.04',
                date=datetime.date(2022, 2, 8)
            ), 'f1590a6e-90ac-492e-b594-aee4b0bd348b': EventRealization(
                event_id='f1590a6e-90ac-492e-b594-aee4b0bd348b',
                room_id='7ae528b9-e0dc-47d4-bfe8-6ebfaa94248c', grid_slot_id='Grid.05.08',
                date=datetime.date(2022, 2, 8)
            ), 'beb4987e-0acc-40e4-9c04-07aeae5a23b9': EventRealization(
                event_id='beb4987e-0acc-40e4-9c04-07aeae5a23b9',
                room_id='80ffcc18-edaf-46e8-9b94-4fab95802660', grid_slot_id='Grid.05.07',
                date=datetime.date(2022, 2, 9)
            ), '2fc5e1ca-48a0-4198-940f-2b3bbb937457': EventRealization(
                event_id='2fc5e1ca-48a0-4198-940f-2b3bbb937457',
                room_id='505f8a0e-21cb-409e-9569-28d638f54418', grid_slot_id='Grid.05.08',
                date=datetime.date(2022, 2, 9)
            ), '81f08e57-f42c-481c-a4ec-bd4f19100bae': EventRealization(
                event_id='81f08e57-f42c-481c-a4ec-bd4f19100bae',
                room_id='4898cdb9-0c5f-4bb9-9c06-01adf5b37463', grid_slot_id='Grid.05.01',
                date=datetime.date(2022, 2, 10)
            ), '27b950aa-05b5-456d-aa56-d882d7260a2f': EventRealization(
                event_id='27b950aa-05b5-456d-aa56-d882d7260a2f',
                room_id='a19f07f5-6bb8-40ac-9d67-801b1bd926ad', grid_slot_id='Grid.05.04',
                date=datetime.date(2022, 2, 10)
            ), 'f58fdc84-57f7-42ac-8f6e-baa018691bfc': EventRealization(
                event_id='f58fdc84-57f7-42ac-8f6e-baa018691bfc',
                room_id='45d573f8-79e2-4159-95a1-e674c102e6d5', grid_slot_id='Grid.05.01',
                date=datetime.date(2022, 2, 11)
            ), '00b90990-8458-491d-a00c-1bbe788e68fe': EventRealization(
                event_id='00b90990-8458-491d-a00c-1bbe788e68fe',
                room_id='4ddece91-af2d-4e0e-babc-e898c4b661f7', grid_slot_id='Grid.05.07',
                date=datetime.date(2022, 2, 11)
            ), '83ef7eea-3ec5-4a98-925a-53761e0caae2': EventRealization(
                event_id='83ef7eea-3ec5-4a98-925a-53761e0caae2',
                room_id='ac7d9d21-5215-49e7-befb-b0ce32712450', grid_slot_id='Grid.05.03',
                date=datetime.date(2022, 2, 11)
            ), 'be0d1ed7-3183-48ae-a903-c15b93a787a5': EventRealization(
                event_id='be0d1ed7-3183-48ae-a903-c15b93a787a5',
                room_id='cc095c4c-8a54-44cc-a054-ed845bbea4d4', grid_slot_id='Grid.05.04',
                date=datetime.date(2022, 2, 11)
            ), 'ddcef7b2-053c-40e0-8442-fec2c4655c4b': EventRealization(
                event_id='ddcef7b2-053c-40e0-8442-fec2c4655c4b',
                room_id='b6c10fec-eef0-438d-bfbb-cfbe5db5379d', grid_slot_id='Grid.05.02',
                date=datetime.date(2022, 2, 11)
            ), '2857df3f-16e4-4317-be18-093da8331fed': EventRealization(
                event_id='2857df3f-16e4-4317-be18-093da8331fed',
                room_id='991db426-0d9c-re11-83db-7d8694db75qe', grid_slot_id='Grid.05.05',
                date=datetime.date(2022, 2, 12)
            ), '3cd56a51-88c7-4a48-8133-f67451982849': EventRealization(
                event_id='3cd56a51-88c7-4a48-8133-f67451982849',
                room_id='0e0d6453-7dac-4917-9317-d338f9c208b7', grid_slot_id='Grid.05.08',
                date=datetime.date(2022, 2, 12)
            ), 'ce727d0c-950b-4165-ad88-4fe638af27cb': EventRealization(
                event_id='ce727d0c-950b-4165-ad88-4fe638af27cb',
                room_id='ghtdb426-0d9c-re11-83db-7d8694db75qr', grid_slot_id='Grid.05.07',
                date=datetime.date(2022, 2, 12)
            )
        }

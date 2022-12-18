import copy
import datetime
import math
import random
import numpy as np
import pandas as pd
from db import Database
from models import (EventRealization, Room, Event)
from collections import Counter
from prettytable import PrettyTable
from data import cycle_realizations, grid_ids

random.seed(4)


# def calculate_exes(data: Database, timetable: dict[str, EventRealization]) -> float:
# x1 - время затраченное в день на переход между корпусами (в день)
# x2 - дней когда пар больше 4 (на неделю, с) +
# x3 - окна (в день с) +
# x4 - переезды (в день)
# x5 - шаговая доступность кафедры (в день, п)
# x6 - концентрированность пар (в день, п)
# x7 - порядок изложения (на неделю)
# x8 - напр 1 знания в 1 корпусе (в день)
# x9 - 1 пара в день (день, с)
# x10 - есть выходной (неделя, с)
# x11 - больше 2 пар в субботу (неделя, с) +

def get_working_days(n_days) -> list[datetime]:
    """Gets all the working days in the semester."""
    working_days: list[datetime] = []
    start = datetime.datetime(2022, 2, 6)
    end = datetime.datetime(2022, 7, 10)
    delta = end - start
    df = pd.read_csv('modeus-data/academic_calendar_irregular_rule.csv')
    if n_days < delta.days + 1:
        for i in range(n_days + 1):
            day = start + datetime.timedelta(days=i)
            if day.date() not in df and day.weekday() != 6:
                working_days.append(day.date())
    else:
        print("You can peak only days that are in the semester")
    return working_days


class TimetableBuilder:
    def __init__(
            self,
            data: Database,
    ):
        self._data = data

    def build_random(self, n_days) -> list[EventRealization]:
        """Builds random timetable for n days. Returns a list of `EventRealization`."""
        working_days = get_working_days(n_days)
        timetable: list[EventRealization] = []
        rooms_sorted = sorted(self._data.rooms, key=lambda x: x.effective_capacity)
        for day in working_days[:n_days + 1]:
            slots = random.choices(grid_ids, k=random.randint(1, 4))
            events = random.choices([event for event in self._data.events if event.capacity_required < 301],
                                    k=len(slots))
            rooms: list[Room] = [
                peak_room(event.capacity_required, rooms_sorted, math.ceil(event.capacity_required / 2))
                for event in events]
            for event, room, slot in zip(events, rooms, slots):
                timetable.append(EventRealization(event.id, room.id, slot, day))
        return timetable

    def build_fixed(self) -> dict[str, EventRealization]:
        """Returns a fixed optimal map of `event_id` to `EventRealization`."""
        return my_timetable_fittest

    def slicer(self, total_weeks: int = 18, slice_weeks: int = 3) -> list[Event]:

        events = sorted([event for event in self._data.events for i in cycle_realizations if
                         event.cycle_realization_id == i], key=lambda x: x.ordinal)
        course_unit_ids = [event.course_unit_id for event in events]

        cycle_realizations_ids = [event.cycle_realization_id for event in events]
        distribution = []
        for i in Counter(course_unit_ids).values():

            if i < total_weeks:
                d = [int(j > total_weeks - i) for j in range(total_weeks, 0, -1)]
                distribution.append(d)
            else:
                d = [1 for _ in range(total_weeks)]
                for j in range(i - total_weeks):
                    d[j] += 1
                distribution.append(d)
        print(sorted(cycle_realizations_ids))
        print(distribution)
        dist_ = [0] * total_weeks
        for i, j in Counter(distribution[1]).items():
            if i == 0:
                continue
            step = total_weeks / j
            for k in range(j):
                index = 0
                startIndex = int(step * k)
                for index in range(startIndex, total_weeks):
                    if dist_[index] == 0:
                        dist_[index] = i
                        break
                if index == total_weeks:
                    for index in range(startIndex, 0, -1):
                        if dist_[index] == 0:
                            dist_[index] = i
                            break
        print(dist_)


class Annealing:
    def __init__(self, data: Database):
        self.TEMPERATURE = 100
        self.TEMPERATURE_FIN = 0.13
        self.COOLING = 0.95
        self.timetable = self.generate_random_population(data)

    def generate_random_population(self, data: Database) -> list[EventRealization]:
        timetable: TimetableBuilder = TimetableBuilder(data)
        random_timetable = timetable.build_random(7)
        return random_timetable

    def swap(self, timetable: list[EventRealization]):
        next = copy.deepcopy(timetable)
        idx = range(len(next))
        i1, i2 = random.sample(idx, 2)
        next[i1].grid_slot_id, next[i2].grid_slot_id = next[i2].grid_slot_id, next[i1].grid_slot_id
        return next

    def run(self):
        k = 0
        while self.TEMPERATURE > self.TEMPERATURE_FIN:
            cur = self.timetable
            next = self.swap(cur)
            h = objective_function(next) - objective_function(cur)
            if h < 0:
                self.TEMPERATURE *= self.COOLING
                self.timetable = next
            else:
                if random.random() < np.exp(-h / self.TEMPERATURE):
                    self.timetable = next
                else:
                    self.timetable = cur
            print(self.TEMPERATURE)
            k += 1
        print(objective_function(self.timetable))
        print("Iterations: ", k)
        for i in sorted(self.timetable, key=lambda x: x.date):
            print(i.event_id, i.room_id, i.grid_slot_id, i.date)


def calculate_x2(timetable: list[EventRealization]) -> int:
    '''Counts the number of days when there are more than 4 study sessions in a timetable.'''
    lessons_per_day = Counter()
    for i in range(len(timetable)):
        lessons_per_day[timetable[i].date] += 1
    lessons = np.array(list(lessons_per_day.values()))
    return np.count_nonzero(lessons > 4)


def calculate_x3(timetable: list[EventRealization]) -> int:
    '''Counts the number of windows between study sessions in a timetable.'''
    grid_slots = list(map(lambda x: int(x.grid_slot_id[-1]), timetable))
    dates = Counter(list(map(lambda x: x.date, timetable)))
    lessons_n = list(dates.values())
    lessons_n.insert(0, 0)
    c = np.cumsum(lessons_n)
    slots = [sorted(grid_slots[c[i - 1]:c[i]]) for i in range(1, len(c))]
    windows_n = [sum(x for x in (np.diff(slot) - 1) if x > 0) for slot in slots]
    return sum(windows_n)


def calculate_x11(timetable: list[EventRealization]) -> int:
    '''Counts the number of Saturdays when there are more than 2 study sessions in a timetable.'''
    saturdays = Counter()
    dates = (np.array(list(map(lambda x: x.date.weekday(), timetable))))
    index = np.where(np.diff(dates) != 0)[0] + 1
    weekdays = np.split(dates, index)
    for weekday in weekdays:
        if weekday[0] == 5 and len(weekday) > 2:
            saturdays["more_2"] += 1
    return len(saturdays)


def calculate_slot_conflicts(timetable: list[EventRealization]) -> int:
    '''Calculates the number of slot conflicts in a timetable.'''
    grid_slot_conflicts = Counter({'time_con': 0})
    for i in range(len(timetable)):
        for j in range(i + 1, len(timetable)):
            if timetable[i].date == timetable[j].date and timetable[i].grid_slot_id == timetable[j].grid_slot_id:
                grid_slot_conflicts["time_con"] += 1
    return list(grid_slot_conflicts.values())[0]


def objective_function(timetable: list[EventRealization]) -> int:
    '''Calculates the fitness of a timetable instance.'''
    conflicts: Counter[str, int] = Counter(
        {"x2": calculate_x2(timetable), "x3": calculate_x3(timetable), "x11": calculate_x11(timetable),
         "slot_con": calculate_slot_conflicts(timetable)})
    return sum(list(conflicts.values()))


def visualize_timetable() -> PrettyTable():
    '''Visualizes list[EventRealization] as a table.'''
    imikn_ex = pd.read_csv('modeus-data/Imikn_ex.csv', encoding='latin-1')
    timetable = PrettyTable(imikn_ex.axes[1].values[0].split(';'))
    rows = [row[0].split(';') for row in imikn_ex.values][::]
    changed = ['-' if rows[i][j] == "null" else rows[i][j] for i in range(len(rows)) for j in range(len(rows[i]))]
    sublists = []
    sublist_len = len(rows[0])
    for i in range(len(rows)):
        sublists.append(changed[sublist_len * i:sublist_len * (i + 1)])
    timetable.add_rows(sublists)
    with open('modeus-data/timetable', 'w') as f:
        f.write(str(timetable))
    return timetable


def peak_room(needed_capacity: int, rooms: list[Room], prec: int) -> Room:
    """Peaks a room for a study session. Deprecated in generating firm timetable"""
    left, right = 0, len(rooms) - 1
    while left <= right:
        mid = (left + right) // 2
        if all(rooms[mid].effective_capacity - i < needed_capacity for i in range(prec + 1)):
            left = mid + 1
        elif all(rooms[mid].effective_capacity - i > needed_capacity for i in range(prec + 1)):
            right = mid - 1
        else:
            return rooms[mid]

import datetime
import math
import random
from collections import Counter
import numpy as np
from db import Database
from models import (
    EventRealization, Room
)
from prettytable import PrettyTable
import pandas as pd
from data import my_event_ids, grid_ids, my_timetable_fittest
from datetime import date
from pymzn import dzn

# random.seed(0)


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

class TimetableBuilder:
    def __init__(
            self,
            data: Database,
    ):
        self._data = data

    def get_working_days(self) -> list[datetime]:
        """Gets all the working days in the semester."""
        working_days: list[datetime] = []
        start = datetime.datetime(2022, 2, 6)
        end = datetime.datetime(2022, 7, 10)
        delta = end - start
        for i in range(delta.days + 1):
            day = start + datetime.timedelta(days=i)
            if day.date() not in self._data.day_offs and day.weekday() != 6:
                working_days.append(day.date())
        return working_days

    def build_random(self, days_n) -> list[EventRealization]:
        """Builds random timetable for n days. Returns a list of `EventRealization`."""
        working_days = self.get_working_days()
        timetable: list[EventRealization] = []
        rooms_sorted = sorted(self._data.rooms, key=lambda x: x.effective_capacity)
        for day in working_days[:days_n + 1]:
            slots = random.choices(grid_ids, k=random.randint(2, 5))
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


class Individual:
    def __init__(self, timetable: list[EventRealization], fitness: int):
        self.timetable = timetable
        self.fitness = fitness


class GeneticAlgorithm:
    def __init__(self, data: Database):
        self.ITERATIONS = 15
        self.POPULATION_SIZE = 1000
        self.MUTATION_PROB = 0.1
        self.MAX_CONFLICTS = 4
        self.selected: list[list[Individual]] = []
        self.initial_population = self.generate_random_population(data)


    def generate_random_population(self, data: Database) -> list[Individual]:
        """Generates random population of size 100."""
        timetable: TimetableBuilder = TimetableBuilder(data)
        population: list[Individual] = []
        for i in range(self.POPULATION_SIZE):
            random_timetable = timetable.build_random(7)
            population.append(Individual(random_timetable, calculate_fitness(random_timetable)))
        return population

    def selection(self, population: list[Individual]) -> list[Individual, Individual]:
        '''Selects 2 individual with a higher fitness from 2 random pairs.'''
        if (first_pair := sorted(random.sample(population, 2),
                                 key=lambda x: x.fitness)) not in self.selected:
            self.selected.append(first_pair)
        if (second_pair := sorted(random.sample(population, 2),
                                  key=lambda x: x.fitness)) not in self.selected:
            self.selected.append(second_pair)
        return [first_pair[0], second_pair[0]]

    def crossover(self, pair: list[Individual, Individual]) -> list[Individual, Individual]:
        n_genes_change = random.randint(1, 2)
        n_crossovers = min(len(pair[0].timetable), len(pair[1].timetable))
        if n_genes_change == 2:
            for i in range(n_crossovers):
                pair[0].timetable[i].grid_slot_id, pair[1].timetable[i].grid_slot_id = \
                    pair[1].timetable[i].grid_slot_id, pair[0].timetable[i].grid_slot_id
                pair[0].timetable[i].date, pair[1].timetable[i].date = \
                    pair[1].timetable[i].date, pair[0].timetable[i].date
        else:
            rnd = random.randint(0, 1)
            if rnd == 0:
                for i in range(n_crossovers):
                    pair[0].timetable[i].grid_slot_id, pair[1].timetable[i].grid_slot_id = \
                        pair[1].timetable[i].grid_slot_id, pair[0].timetable[i].grid_slot_id
            else:
                for i in range(n_crossovers):
                    pair[0].timetable[i].date, pair[1].timetable[i].date = \
                        pair[1].timetable[i].date, pair[0].timetable[i].date
        for i in range(2):
            pair[i].fitness = calculate_fitness(pair[i].timetable)
            print(pair[i].fitness)
        return pair

    def mutation(self, individual: Individual) -> Individual:
        rnd = random.randint(0, 1)
        n = int(len(individual.timetable) * self.MUTATION_PROB)
        indices_to_change = random.choices(list(range(len(individual.timetable))), k=n)
        if rnd == 0:
            for i in range(n):
                cur_grid_slot_id = individual.timetable[indices_to_change[i]].grid_slot_id
                individual.timetable[indices_to_change[i]].grid_slot_id = random.choice(
                    [i.grid_slot_id for i in individual.timetable if i.grid_slot_id != cur_grid_slot_id])

        else:
            for i in range(n):
                cur_date = individual.timetable[indices_to_change[i]].date
                individual.timetable[indices_to_change[i]].date = random.choice(
                    [i.date for i in individual.timetable if i.grid_slot_id != cur_date])
        individual.fitness = calculate_fitness(individual.timetable)
        return individual

    def run(self, data: Database) -> list[Individual]:
        '''Runs GA to find an optimized timetable'''
        populations = [self.initial_population]
        for j in (range(self.ITERATIONS)):
            next_population: list[Individual] = []
            for i in range(self.POPULATION_SIZE // 2):
                selected = self.selection(populations[j])
                cross_pair = self.crossover(selected)
                if selected[0].fitness < cross_pair[0].fitness:
                    cross_pair[0] = selected[0]
                if selected[1].fitness < cross_pair[1].fitness:
                    cross_pair[1] = selected[1]
                if cross_pair[0].fitness < self.MAX_CONFLICTS or cross_pair[1].fitness < self.MAX_CONFLICTS:
                    return cross_pair
                else:
                    next_population.append(cross_pair[0])
                    next_population.append(cross_pair[1])
            if random.random() <= self.MUTATION_PROB:
                rnd_idx = random.randint(0, len(next_population) - 1)
                next_population[rnd_idx] = self.mutation(next_population[rnd_idx])
            populations.append(next_population)
        return populations[-1]


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


def calculate_fitness(timetable: list[EventRealization]) -> int:
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
    """Peaks a room for a study session."""
    left, right = 0, len(rooms) - 1
    while left <= right:
        mid = (left + right) // 2
        if all(rooms[mid].effective_capacity - i < needed_capacity for i in range(prec + 1)):
            left = mid + 1
        elif all(rooms[mid].effective_capacity - i > needed_capacity for i in range(prec + 1)):
            right = mid - 1
        else:
            return rooms[mid]

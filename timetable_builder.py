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
        for day in working_days[:7]:
            slots = random.choices(grid_slots_uni, k=random.randint(2, 5))
            rooms = []
            events = random.choices(
                [event for event in self._data.events if event.capacity_required < 301],
                k=len(slots)
            )
            for event in events:
                peaked = peak_room(
                    event.capacity_required, rooms_sorted, math.ceil(event.capacity_required * 0.46)
                )
                rooms.append(peaked)

            for event, room, slot in zip(events, rooms, slots):
                timetable.setdefault(
                    event.id, EventRealization(event.id, room.id, slot.id, day)
                )
            file = open("timetable.txt", 'w')
            file.write(str(timetable))
        return timetable

    def build_optimized(self) -> dict[str, EventRealization]:
        """Builds optimized timetable. Returns a map of `event_id` to `EventRealization`."""
        raise NotImplementedError

    def build_fixed(self) -> dict[str, EventRealization]:
        """Returns a fixed optimal map of `event_id` to `EventRealization`."""
        timetable = {
            'ea70e3d4-ddc8-474d-91ba-128f86dbd387': EventRealization(
                event_id='ea70e3d4-ddc8-474d-91ba-128f86dbd387',
                room_id='a5be3cfe-6d27-4f25-9030-a81a94590190', grid_slot_id='Grid.05.04',
                date=datetime.date(2022, 2, 7)
            ), '6647b181-c1d0-4d9a-ba93-dda830c56eea': EventRealization(
                event_id='6647b181-c1d0-4d9a-ba93-dda830c56eea',
                room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.06',
                date=datetime.date(2022, 2, 7)
            ), '27b7d7b7-4344-470a-b3c2-aa5e8a771b92': EventRealization(
                event_id='27b7d7b7-4344-470a-b3c2-aa5e8a771b92',
                room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.06',
                date=datetime.date(2022, 2, 8)
            ), 'ae4f1ff0-4273-49e3-b82a-b49919c599ab': EventRealization(
                event_id='ae4f1ff0-4273-49e3-b82a-b49919c599ab',
                room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.02',
                date=datetime.date(2022, 2, 8)
            ), '34a6f40a-c3b0-4cda-ac77-c15a2b534e53': EventRealization(
                event_id='34a6f40a-c3b0-4cda-ac77-c15a2b534e53',
                room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.03',
                date=datetime.date(2022, 2, 8)
            ), '09edd499-3b31-4358-9e54-b457b344a713': EventRealization(
                event_id='09edd499-3b31-4358-9e54-b457b344a713',
                room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.03',
                date=datetime.date(2022, 2, 8)
            ), 'a06ca092-b6e2-4ef7-b82d-490714f16d89': EventRealization(
                event_id='a06ca092-b6e2-4ef7-b82d-490714f16d89',
                room_id='e17b77cf-c3cc-485f-b05f-cc3194caa915', grid_slot_id='Grid.05.01',
                date=datetime.date(2022, 2, 9)
            ), 'f1b26f42-9b1c-419a-8db6-bc179a87b295': EventRealization(
                event_id='f1b26f42-9b1c-419a-8db6-bc179a87b295',
                room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.07',
                date=datetime.date(2022, 2, 9)
            ), 'f1561bb6-6a94-4a80-959f-9bec5b42c1ee': EventRealization(
                event_id='f1561bb6-6a94-4a80-959f-9bec5b42c1ee',
                room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.07',
                date=datetime.date(2022, 2, 9)
            ), '719d1238-99d8-4ee5-a113-ed7a35cacc9c': EventRealization(
                event_id='719d1238-99d8-4ee5-a113-ed7a35cacc9c',
                room_id='a5be3cfe-6d27-4f25-9030-a81a94590190', grid_slot_id='Grid.05.06',
                date=datetime.date(2022, 2, 9)
            ), 'c66466e1-2bae-46a5-97a7-b7279ea0c639': EventRealization(
                event_id='c66466e1-2bae-46a5-97a7-b7279ea0c639',
                room_id='e17b77cf-c3cc-485f-b05f-cc3194caa915', grid_slot_id='Grid.05.06',
                date=datetime.date(2022, 2, 10)
            ), 'e08e2e07-6487-4739-8796-70b12ee6f70f': EventRealization(
                event_id='e08e2e07-6487-4739-8796-70b12ee6f70f',
                room_id='a5be3cfe-6d27-4f25-9030-a81a94590190', grid_slot_id='Grid.05.07',
                date=datetime.date(2022, 2, 10)
            ), 'a7ca5e64-549f-4d07-afc2-547524582be5': EventRealization(
                event_id='a7ca5e64-549f-4d07-afc2-547524582be5',
                room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.07',
                date=datetime.date(2022, 2, 10)
            ), 'adb70926-92fa-494f-9359-51208122edc3': EventRealization(
                event_id='adb70926-92fa-494f-9359-51208122edc3',
                room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.06',
                date=datetime.date(2022, 2, 10)
            ), 'd0276f08-61c7-4006-9062-deb743c56896': EventRealization(
                event_id='d0276f08-61c7-4006-9062-deb743c56896',
                room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.06',
                date=datetime.date(2022, 2, 10)
            ), 'b0909730-5c06-4d85-8628-2260536bf065': EventRealization(
                event_id='b0909730-5c06-4d85-8628-2260536bf065',
                room_id='f7e3c952-f2de-450d-b447-d72de1e26159', grid_slot_id='Grid.05.06',
                date=datetime.date(2022, 2, 11)
            ), 'a7000683-3113-4d57-90a9-787ebfb866b9': EventRealization(
                event_id='a7000683-3113-4d57-90a9-787ebfb866b9',
                room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.06',
                date=datetime.date(2022, 2, 11)
            ), '54d2a24a-6681-49ed-8128-7b8eee9d30a8': EventRealization(
                event_id='54d2a24a-6681-49ed-8128-7b8eee9d30a8',
                room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.01',
                date=datetime.date(2022, 2, 11)
            ), '450841db-d7b0-4f6b-afbf-281c3d0f7da4': EventRealization(
                event_id='450841db-d7b0-4f6b-afbf-281c3d0f7da4',
                room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.03',
                date=datetime.date(2022, 2, 12)
            ), '8123d3b2-d7b0-4297-a3b4-76ef5e5daa00': EventRealization(
                event_id='8123d3b2-d7b0-4297-a3b4-76ef5e5daa00',
                room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.05',
                date=datetime.date(2022, 2, 12)
            ), 'afe85cb1-ff67-40a2-b971-0898d427a0f9': EventRealization(
                event_id='afe85cb1-ff67-40a2-b971-0898d427a0f9',
                room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.07',
                date=datetime.date(2022, 2, 12)
            ), '71b16219-4e31-4032-9277-8f49af1ff798': EventRealization(
                event_id='71b16219-4e31-4032-9277-8f49af1ff798',
                room_id='a5be3cfe-6d27-4f25-9030-a81a94590190', grid_slot_id='Grid.05.01',
                date=datetime.date(2022, 2, 14)
            ), 'b23106a4-6378-4ba2-a650-0eeb4936d6fe': EventRealization(
                event_id='b23106a4-6378-4ba2-a650-0eeb4936d6fe',
                room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.01',
                date=datetime.date(2022, 2, 14)
            ), 'd5c4b0a5-95ca-475b-ab4c-60a535573494': EventRealization(
                event_id='d5c4b0a5-95ca-475b-ab4c-60a535573494',
                room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.07',
                date=datetime.date(2022, 2, 14)
            ), 'a1a460d6-1379-49ea-b841-f5157573bb17': EventRealization(
                event_id='a1a460d6-1379-49ea-b841-f5157573bb17',
                room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.01',
                date=datetime.date(2022, 2, 14)
            )
        }
        return timetable


class Individual:
    def __init__(self, ttb: dict[str, EventRealization], fitness: float):
        self.ttb = ttb
        self.fitness = fitness


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


def calculate_x2(timetable: list[EventRealization]) -> int:
    lessons_per_day = Counter()
    for i in range(len(timetable)):
        lessons_per_day[timetable[i].date] += 1
    lessons = np.array(list(lessons_per_day.values()))
    return np.count_nonzero(lessons > 4)


def calculate_x3(timetable: list[EventRealization]) -> int:
    lessons_per_day = Counter()
    slots_each_day = []
    windows = []
    grid_slots = list(map(lambda x: int(x.grid_slot_id[-1]), timetable))
    for i in range(len(timetable)):
        lessons_per_day[timetable[i].date] += 1
    cum = list(np.cumsum(list(lessons_per_day.values())))
    cum.insert(0, 0)
    for i in range(1, len(cum)):
        slots_each_day.append(grid_slots[cum[i - 1]:cum[i]])
    for slots in slots_each_day:
        slots = sorted(slots)
        for i in range(1, len(slots)):
            if (time_dif := slots[i] - slots[i - 1]) > 1:
                windows.append(time_dif - 1)
    return sum(windows)


def calculate_x11(timetable: list[EventRealization]) -> int:
    saturdays = Counter()
    dates = (np.array(list(map(lambda x: x.date.weekday(), timetable))))
    index = np.where(np.diff(dates) != 0)[0] + 1
    weekdays = np.split(dates, index)
    for weekday in weekdays:
        if weekday[0] == 5 and len(weekday) > 2:
            saturdays["more_2"] += 1
    return len(saturdays)


def calculate_fitness(data: Database, timetable: dict[str, EventRealization]) -> float:
    classes = list(timetable.values())
    conflicts: Counter[str, int] = Counter()
    # for i in range(len(classes)):
    #     for j in range(i + 1, len(classes)):
    #         if classes[i].date == classes[j].date:
    #             if classes[i].grid_slot_id == classes[j].grid_slot_id:
    #                 conflicts["time_con"] += 1
    #
    #     if data.get_room(classes[i].room_id).effective_capacity < len(
    #             data.get_event_attendees_by_event(classes[i].event_id)
    #     ):
    #         conflicts["capacity_con"] += 1
    conflicts["x2"] = calculate_x2(classes)
    conflicts["x3"] = calculate_x3(classes)
    conflicts["x11"] = calculate_x11(classes)
    return 1 / (1 + sum(list(conflicts.values())))


# сделать таблицу на имикн
def pop_formation(data: Database, n_pop: int = 100):
    random.seed(0)
    ttb = TimetableBuilder(data)
    population = []
    for i in range(n_pop):
        rnd_ttb = ttb.build_random()
        population.append(Individual(rnd_ttb, calculate_fitness(data, rnd_ttb)))
    return population


#  Warning: tournament selection already chosen pairs are possible
def tournament_selection(population: list[Individual]) -> list[Individual]:
    CROSSOVER_PROB = 0.9
    MUTATION_PROB = 0.1
    fst_pair = np.random.choice(population, 2)
    scnd_pair = np.random.choice(population, 2)
    fittest_couple = [max(fst_pair, key=lambda x: x.fitness), max(scnd_pair, key=lambda x: x.fitness)]
    # action = random.choices([crossver(fittest_couple), ])
    # return


def crossover(couple: list[Individual]) -> list[dict[str, EventRealization]]:
    partner_1 = list(couple[0].ttb.values())
    partner_2 = list(couple[1].ttb.values())
    crossovers_n = min(len(partner_1), len(partner_2))
    for i in range(crossovers_n):
        partner_1[i].grid_slot_id, partner_2[i].grid_slot_id = partner_2[i].grid_slot_id, partner_1[i].grid_slot_id
        partner_1[i].date, partner_2[i].date = partner_2[i].date, partner_1[i].date
    couple[0].ttb = partner_1
    couple[1].ttb = partner_2
    return [couple[0].ttb, couple[1].ttb]


def mutation(data: Database, individual: Individual) -> dict[str, EventRealization]:
    pos_to_change = random.randint(0, len(list(individual.ttb.values())))
    what_to_change = random.randint(0, 1)
    for i in range(len(individual.ttb.values())):
        if i == pos_to_change:
            if what_to_change == 0:
                list(individual.ttb.values())[pos_to_change].grid_slot_id = data.grid_slots[
                    random.randint(0, len(data.grid_slots))]
            else:
                list(individual.ttb.values())[pos_to_change].date = random.choice(
                    list(individual.ttb.values())[random.randint(0, len(list(individual.ttb.values())))]).date


def visualise_timetable(timetable: dict[str, EventRealization]) -> PrettyTable():
    print(list(timetable.values()))
    # lessons = [data.get_course_unit(list(i.keys())[0]).name for i in subjects]
    # x = PrettyTable(["Time", "306", "404", "423"])
    # rows = [
    #     ["8:30-10:00", "-", "-", "-"],
    #     ["10:15-11:45", "-", "-", "-"],
    #     ["12:00-13:30", "-", "-", "-"],
    #     ["14:00-15:30", "-", "-", "-"],
    #     ["15:45-17:15", "-", "-", "-"],
    #     ["15:45-17:15", "-", "-", "-"],
    #     ["17:00-19:00", "-", "-", "-"],
    #     ["19:10-20:40", "-", "-", "-"],
    #     ["20:50-22:20", "-", "-", "-"]
    # ]
    #
    # n = [i for i in range(9)]
    # res = [[n[i], n[i + 1], n[i + 2]]
    #        for i in range(len(n) - 2)]
    # times = random.choice(res)
    #
    # rows[times[0]][1] = lessons[0]
    # rows[times[1]][2] = lessons[1]
    # rows[times[2]][3] = lessons[2]
    #
    # x.add_rows(rows)
    # print(x)
    # lessons = [data.get_course_unit(list(i.keys())[0]).name for i in subjects]

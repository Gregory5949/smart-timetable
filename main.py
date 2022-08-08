import logging
import datetime
import random
from pathlib import Path
from pprint import pprint
from db import Database
from models import EventRealization
from timetable_builder import TimetableBuilder, calculate_fitness, pop_formation, calculate_x3, calculate_x2, \
    calculate_x11, tournament_selection
from data import *

logging.basicConfig(level=logging.INFO)


def main():
    # Read data
    # random.seed(0)
    data = Database()
    data.load_from_dir(Path("modeus-data"))
    # population = pop_formation(data)
    # next_population = []
    # print(tournament_selection(population))
    # while len(next_population) < len(population):
    #     fittest_pair = tournament_selection(population)
    #     next_population.append(fittest_pair[0])
    #     next_population.append(fittest_pair[1])
    # print(next_population)
    # print([population[i].fitness for i in range(len(population))])

    # # Build timetable
    ttb = TimetableBuilder(data)
    logging.info("Building random timetable...")
    built_ttb = ttb.build_random()
    print(built_ttb.values())
    # print(calculate_fitness(data,built_ttb))
    timetables = []
    fitness = []

    # for i in range(5):
    #     ttb = TimetableBuilder(data).build_random()
    #     _fitness = calculate_fitness(data, ttb)
    #     print(_fitness)
    #     fitness.append(_fitness)
    #     timetables.append(ttb)
    # fittest = selection(data, timetables)
    # print(fittest[0])
    # print(fitness[timetables.index(fittest[0])])

    fittest = {'44664573-332c-4df1-ac32-7cf2c7ac694f': EventRealization(event_id='44664573-332c-4df1-ac32-7cf2c7ac694f',
                                                                        room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21',
                                                                        grid_slot_id='Grid.05.06',
                                                                        date=datetime.date(2022, 2, 7)),
               '82a74e27-a930-452e-8416-58870411307a': EventRealization(event_id='82a74e27-a930-452e-8416-58870411307a',
                                                                        room_id='1645c9e5-eafe-4c3a-a12a-7f5a62792ab8',
                                                                        grid_slot_id='Grid.05.03',
                                                                        date=datetime.date(2022, 2, 7)),
               'a91dd5cd-5c6b-4284-a95b-e9c357c9ec21': EventRealization(event_id='a91dd5cd-5c6b-4284-a95b-e9c357c9ec21',
                                                                        room_id='8cf16536-8a8d-4a92-97a6-39626504a927',
                                                                        grid_slot_id='Grid.05.01',
                                                                        date=datetime.date(2022, 2, 7)),
               'e1d577b8-8cea-4b5c-a7e4-9624b803938c': EventRealization(event_id='e1d577b8-8cea-4b5c-a7e4-9624b803938c',
                                                                        room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56',
                                                                        grid_slot_id='Grid.05.02',
                                                                        date=datetime.date(2022, 2, 7)),
               '97e9a197-713c-4570-9726-ac9a9abd2387': EventRealization(event_id='97e9a197-713c-4570-9726-ac9a9abd2387',
                                                                        room_id='1645c9e5-eafe-4c3a-a12a-7f5a62792ab8',
                                                                        grid_slot_id='Grid.05.05',
                                                                        date=datetime.date(2022, 2, 8)),
               '5aa3f9b8-0b1f-4409-8ec9-ed5e68515dab': EventRealization(event_id='5aa3f9b8-0b1f-4409-8ec9-ed5e68515dab',
                                                                        room_id='5d1b3245-b89a-4e38-97f9-9840b9604842',
                                                                        grid_slot_id='Grid.05.03',
                                                                        date=datetime.date(2022, 2, 8)),
               'c3faff14-8482-4b30-9432-106b4f033825': EventRealization(event_id='c3faff14-8482-4b30-9432-106b4f033825',
                                                                        room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe',
                                                                        grid_slot_id='Grid.05.01',
                                                                        date=datetime.date(2022, 2, 8)),
               'bcec138b-2c8f-48d8-81c6-64305ad1eea5': EventRealization(event_id='bcec138b-2c8f-48d8-81c6-64305ad1eea5',
                                                                        room_id='a5be3cfe-6d27-4f25-9030-a81a94590190',
                                                                        grid_slot_id='Grid.05.07',
                                                                        date=datetime.date(2022, 2, 8)),
               '773b9b4f-dfeb-4839-8f4f-a2b742e8b15d': EventRealization(event_id='773b9b4f-dfeb-4839-8f4f-a2b742e8b15d',
                                                                        room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21',
                                                                        grid_slot_id='Grid.05.02',
                                                                        date=datetime.date(2022, 2, 8)),
               '15c65bcf-f715-4163-95ac-42976574b2f1': EventRealization(event_id='15c65bcf-f715-4163-95ac-42976574b2f1',
                                                                        room_id='5d1b3245-b89a-4e38-97f9-9840b9604842',
                                                                        grid_slot_id='Grid.05.08',
                                                                        date=datetime.date(2022, 2, 9)),
               '5632a274-91ee-4ef5-92d5-f49c147db4d5': EventRealization(event_id='5632a274-91ee-4ef5-92d5-f49c147db4d5',
                                                                        room_id='5d1b3245-b89a-4e38-97f9-9840b9604842',
                                                                        grid_slot_id='Grid.05.05',
                                                                        date=datetime.date(2022, 2, 9)),
               'e984db95-4307-4ac4-9fb5-bc909547ff8d': EventRealization(event_id='e984db95-4307-4ac4-9fb5-bc909547ff8d',
                                                                        room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56',
                                                                        grid_slot_id='Grid.05.02',
                                                                        date=datetime.date(2022, 2, 10)),
               'a8de96f6-6e24-4efc-aedc-025eab317b69': EventRealization(event_id='a8de96f6-6e24-4efc-aedc-025eab317b69',
                                                                        room_id='8dcbd51f-71c6-4f97-8ef5-5f258dbca1f5',
                                                                        grid_slot_id='Grid.05.01',
                                                                        date=datetime.date(2022, 2, 10)),
               '4c50ace3-536e-4fc3-a675-055c1b5af493': EventRealization(event_id='4c50ace3-536e-4fc3-a675-055c1b5af493',
                                                                        room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56',
                                                                        grid_slot_id='Grid.05.03',
                                                                        date=datetime.date(2022, 2, 10)),
               'e2f3d7d2-5a4c-420f-88f5-330f4faafea1': EventRealization(event_id='e2f3d7d2-5a4c-420f-88f5-330f4faafea1',
                                                                        room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21',
                                                                        grid_slot_id='Grid.05.06',
                                                                        date=datetime.date(2022, 2, 11)),
               '61c4331f-9a48-439c-a9d9-0a136e88f168': EventRealization(event_id='61c4331f-9a48-439c-a9d9-0a136e88f168',
                                                                        room_id='5d1b3245-b89a-4e38-97f9-9840b9604842',
                                                                        grid_slot_id='Grid.05.07',
                                                                        date=datetime.date(2022, 2, 11)),
               '295907a7-2ba1-44e8-aedf-e4400c630f04': EventRealization(event_id='295907a7-2ba1-44e8-aedf-e4400c630f04',
                                                                        room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe',
                                                                        grid_slot_id='Grid.05.05',
                                                                        date=datetime.date(2022, 2, 11)),
               '120c2cc0-3c5e-4994-9274-ba2c61573d14': EventRealization(event_id='120c2cc0-3c5e-4994-9274-ba2c61573d14',
                                                                        room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe',
                                                                        grid_slot_id='Grid.05.07',
                                                                        date=datetime.date(2022, 2, 12)),
               'b22d0c55-00bd-4721-ab90-0881e7ba719e': EventRealization(event_id='b22d0c55-00bd-4721-ab90-0881e7ba719e',
                                                                        room_id='e17b77cf-c3cc-485f-b05f-cc3194caa915',
                                                                        grid_slot_id='Grid.05.01',
                                                                        date=datetime.date(2022, 2, 12)),
               '1cb6df37-e02c-4b3d-a5e0-873cc9706c25': EventRealization(event_id='1cb6df37-e02c-4b3d-a5e0-873cc9706c25',
                                                                        room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21',
                                                                        grid_slot_id='Grid.05.05',
                                                                        date=datetime.date(2022, 2, 12)),
               'e191f91e-6eaa-499c-8c29-4064dbc99ad3': EventRealization(event_id='e191f91e-6eaa-499c-8c29-4064dbc99ad3',
                                                                        room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56',
                                                                        grid_slot_id='Grid.05.03',
                                                                        date=datetime.date(2022, 2, 12)),
               '3e7d35a5-976a-449a-a0a2-95118e79b5e2': EventRealization(event_id='3e7d35a5-976a-449a-a0a2-95118e79b5e2',
                                                                        room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe',
                                                                        grid_slot_id='Grid.05.07',
                                                                        date=datetime.date(2022, 2, 12)),
               'e108bf3a-b6cc-432f-93b3-14d473935aad': EventRealization(event_id='e108bf3a-b6cc-432f-93b3-14d473935aad',
                                                                        room_id='8cf16536-8a8d-4a92-97a6-39626504a927',
                                                                        grid_slot_id='Grid.05.04',
                                                                        date=datetime.date(2022, 2, 14)),
               '065ebc75-5b1b-4b5b-8f74-deaff7988836': EventRealization(event_id='065ebc75-5b1b-4b5b-8f74-deaff7988836',
                                                                        room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe',
                                                                        grid_slot_id='Grid.05.03',
                                                                        date=datetime.date(2022, 2, 14)),
               '8d4899a5-63ec-4226-bc3d-9671bcceb06f': EventRealization(event_id='8d4899a5-63ec-4226-bc3d-9671bcceb06f',
                                                                        room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21',
                                                                        grid_slot_id='Grid.05.03',
                                                                        date=datetime.date(2022, 2, 14))}
    # print(calculate_fitness(data, fittest))
    # print(calculate_fitness(data, fittest))
    # print(len(data.get_event_attendees_by_event("00007622-a5a3-4eb9-a7b5-9b85db5673e0")))
    # Show fittest
    # logging.info("finding fittest from a population of 100...")
    # ttb = TimetableBuilder(data)
    # population = ttb.build_optimized()
    # file = open('timetable.txt', 'w')
    # file.write(str(built_ttb))
    # file = open('timetable.txt', 'w')
    # file.write(str(selection(population)))
    # pprint(selection(population), width=120)
    # pprint(data.events)
    #  Count conflicts
    # logging.info("Conflicts...")
    # conflicts = count_conflicts(data, built_ttb)
    # pprint(conflicts)
    # logging.info("Script finished")


if __name__ == "__main__":
    main()

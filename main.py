import logging
from prettytable import PrettyTable
from pathlib import Path
from timetable_builder import *

logging.basicConfig(level=logging.INFO)


def main():
    # Read data
    data = Database()
    data.load_from_dir(Path("modeus-data"))
    genetic_algorithm = GeneticAlgorithm(data)
    next = genetic_algorithm.run(data)
    for i in range(len(next)):
        print(len(next[i].timetable))
    best = sorted(next, reverse=True, key=lambda x: x.fitness)[0]
    print(best.fitness, best.timetable)
    # best_so_far = [EventRealization(event_id='1eb84683-1a06-4d9f-874b-f9c0dc4e5b92', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 7)), EventRealization(event_id='0f326112-9b63-430f-9bd8-5a901cd64804', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 7)), EventRealization(event_id='d7adb6da-dbdf-4450-aacd-5d21cfc21a8f', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 8)), EventRealization(event_id='283180e8-b6c3-481a-9f68-e236614c687e', room_id='e804bb6c-d9d3-46c3-9b3f-2676e26b16ea', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 8)), EventRealization(event_id='ff1ba67f-a3a6-4e51-8192-6b37f0525416', room_id='8cf16536-8a8d-4a92-97a6-39626504a927', grid_slot_id='Grid.05.08', date=datetime.date(2022, 2, 9)), EventRealization(event_id='f9f64eb6-4126-447b-b68f-a28bf12b3156', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.07', date=datetime.date(2022, 2, 9)), EventRealization(event_id='02c7a275-d43f-4c2f-82c3-7e99c5c4b988', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 9)), EventRealization(event_id='4ac9499c-26a1-44da-96ab-c2e8ea4418a4', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 10)), EventRealization(event_id='ef4b90de-9339-4a9c-b4c7-1766edf80a6d', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.08', date=datetime.date(2022, 2, 7)), EventRealization(event_id='56bded4e-fda1-434a-a78f-780d814a3109', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.07', date=datetime.date(2022, 2, 11)), EventRealization(event_id='eee0c762-0209-4c55-a141-f078448aa910', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.07', date=datetime.date(2022, 2, 9)), EventRealization(event_id='a5533a3a-a251-4737-aaa8-caca04a2829a', room_id='8cf16536-8a8d-4a92-97a6-39626504a927', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 11)), EventRealization(event_id='affa2ecd-f7a5-4342-ba7a-d15c1fd21163', room_id='8cf16536-8a8d-4a92-97a6-39626504a927', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 12)), EventRealization(event_id='edab2ce4-1204-409b-82f4-093606ff029e', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 12)), EventRealization(event_id='66884daa-75e4-4c61-b3a0-85d9a63589e3', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 12)), EventRealization(event_id='8c1b4486-102e-466f-b333-c6d1e26ca9a1', room_id='e40dff05-196e-4eca-9d1e-ce1d866311a1', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 12)), EventRealization(event_id='d0796f95-2f0e-4bea-9398-c0cc42df493d', room_id='8cf16536-8a8d-4a92-97a6-39626504a927', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 14))]
    # for i in  best_so_far:
    #     print(i.event_id, i.room_id, i.grid_slot_id, i.date)


if __name__ == "__main__":
    main()

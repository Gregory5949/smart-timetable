import logging
from pathlib import Path
from pprint import pprint
import pymysql
from db import Database
from timetable_builder import TimetableBuilder, calculate_fitness, selection
from data import *

logging.basicConfig(level=logging.INFO)


def main():
    # Read data
    data = Database()
    data.load_from_dir(Path("modeus-data"))
    # Build timetable
    ttb = TimetableBuilder(data)
    logging.info("Building random timetable...")
    built_ttb = ttb.build_random()
    timetables = []
    ttb = TimetableBuilder(data)
    for i in range(100):
        timetables.append(ttb.build_random())
    print(selection(data, timetables))

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

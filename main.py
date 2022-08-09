import csv
import logging
import datetime
import random
import itertools
from pathlib import Path
from pprint import pprint
from db import Database
from models import EventRealization
# from timetable_builder import *
from data import *
from prettytable import PrettyTable
import pandas as pd

logging.basicConfig(level=logging.INFO)


def main():

    print(sorted((2,5)) == sorted((5,2))
          )
    # Read data
    # data = Database()
    # data.load_from_dir(Path("modeus-data"))
    # pop = pop_formation(data)
    # print(genetic_algorithm(data, pop))
    # unique = set()
    # for i in range(50):
    #     selected = tournament_selection(data, pop)
    #     unique.add(list(selected[0].timetable.values())[0].event_id)
    #     unique.add(list(selected[1].timetable.values())[0].event_id)
    # print(len(unique))
    # timetable = list(timetable.values())
    # print(grid_slot_conflicts(timetable))
    # for i in timetable:
    #     print(i.event_id, i.room_id, i.grid_slot_id, i.date, '\n')

#6f20557c-4f92-459d-a965-65fe2011da16 - e82a82e7-94ba-4b28-b996-2615d47d1114
#5dcc6f7c-0c35-4290-9113-18f394199aeb - c348256d-12cf-42bd-8bd6-1026a771a4ba
if __name__ == "__main__":
    main()

import logging
import datetime
import random
import itertools
from pathlib import Path
from pprint import pprint
from db import Database
from models import EventRealization
from timetable_builder import *
from data import *
from prettytable import PrettyTable

logging.basicConfig(level=logging.INFO)


def main():
    # Read data
    random.seed(0)
    data = Database()
    data.load_from_dir(Path("modeus-data"))
    population = pop_formation(data)
    couple = tournament_selection(population)
    for i in couple:
        print(i.ttb)
    print(crossover(couple))

    # next_population = []
    # print(tournament_selection(population))
    # while len(next_population) < len(population):
    #     fittest_pair = tournament_selection(population)
    #     next_population.append(fittest_pair[0])
    #     next_population.append(fittest_pair[1])
    # print(next_population)
    # print([population[i].fitness for i in range(len(population))])

    # # Build timetable
    # ttb = TimetableBuilder(data)
    # logging.info("Building random timetable...")
    # built_ttb = ttb.build_random()
    # print(built_ttb.values())
    # print(calculate_fitness(data,built_ttb))




if __name__ == "__main__":
    main()

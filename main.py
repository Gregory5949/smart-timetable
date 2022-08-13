import logging
import transliterate
from pathlib import Path
import pymysql
from timetable_builder import *

logging.basicConfig(level=logging.INFO)


def main():
    data = Database()
    data.load_from_dir(Path("modeus-data"))
    genetic_algorithm = GeneticAlgorithm(data)
    first_population = genetic_algorithm.initial_population
    final_population = genetic_algorithm.run(data)
    best_first_population = sorted(first_population, key=lambda x: x.fitness)[0]
    best_final_population = sorted(final_population, key=lambda x: x.fitness)[0]
    print("First population", '\n', "Fitness: ", best_first_population.fitness)

    print("Final population", '\n', "Fitness: ", best_final_population.fitness)
    print(calculate_fitness(best_final_population.timetable))
    for i in best_final_population.timetable:

        print(i.event_id, i.room_id, i.grid_slot_id, i.date)


def create_connection(host_name, port, user_name, user_password, db_name):
    connection = None
    try:
        connection = pymysql.connect(
            host=host_name,
            port=port,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Exception as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Exception as e:
        print(f"The error '{e}' occurred")


def data_to_dzn(data: Database, events_n: int):
    events = random.choices(data.events, k=events_n)
    courses: set[str] = set()
    amount_of_students: list[int] = []
    classes: set[str] = set()
    capacity: list[int] = []
    for event in events:
        courses.add(transliterate.translit(event.name, 'ru', reversed=True))
        amount_of_students.append(event.capacity_required)
        room = peak_room(event.capacity_required, sorted(data.rooms, key=lambda x: x.effective_capacity), 1)
        classes.add(transliterate.translit(room.name, 'ru', reversed=True))
        capacity.append(room.effective_capacity)
    data_to_dzn = {
        "COURSES": courses,
        "amount_of_students": amount_of_students,
        "CLASSES": classes,
        "capacity": capacity,
    }
    with open("data.dzn", "w") as f:
        f.write('\n'.join(dzn.dict2dzn(data_to_dzn)))


if __name__ == "__main__":
    main()

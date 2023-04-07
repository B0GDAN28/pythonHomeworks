import csv
import shutil
import os
import json
import uuid

OUTPUT_DIRECTORY = "output_data"
CATEGORIES = {
    "slow_cars": lambda car: car["HP"] < 120,
    "fast_cars": lambda car: 120 <= car["HP"] < 180,
    "sport_cars": lambda car: car["HP"] > 180,
    "cheap_cars": lambda car: car["PRICE"] < 1000,
    "medium_cars": lambda car: 1000 <= car["PRICE"] < 5000,
    "expensive_cars": lambda car: car["PRICE"] > 5000,

}


def clean_up_directories():
    shutil.rmtree("OUTPUT_DIRECTORY", ignore_errors=True)
    os.makedirs("OUTPUT_DIRECTORY")


def get_input():
    data = []
    with open("input.csv") as file:
        csv_dict_reader = csv.DictReader(file)
        for car in csv_dict_reader:
            current_car = {
                "id": str(uuid.uuid4()),
                "HP": int(car.pop("HP")),
                "PRICE": float(car.pop("PRICE"))
            }
            current_car.update(car)
            data.append(current_car)

    return data


def process_data(cars: list):
    # slow_cars = [car for car in cars if car["HP"] < 120]
    # fast_cars = [car1 for car1 in cars if 120 <= car1["HP"] < 180]
    # sport_cars = [car2 for car2 in cars if car2["HP"] >= 180]
    # cheap_cars = [car3 for car3 in cars if car3["PRICE"] < 1000]
    # medium_cars = [car4 for car4 in cars if 1000 <= car4["PRICE"] < 5000]
    # expensive_cars = [car5 for car5 in cars if car5["PRICE"] > 5000]
    #
    # write_to_file("slow_cars.json", slow_cars)
    # write_to_file("fast_cars.json", fast_cars)
    # write_to_file("sports_cars.json", sport_cars)
    # write_to_file("cheap_cars.json", cheap_cars)
    # write_to_file("medium_cars.json", medium_cars)
    # write_to_file("expensive_cars.json", expensive_cars)
    for key, condition_function in CATEGORIES.items():
        data = [car for car in cars if condition_function(car)]
        write_to_file(f"{key}.json", data)


def write_to_file(file_name: str, cars1: list):
    with open(f"output_data/{file_name}", "w") as file:
        json.dump(cars1, file, indent=2)


if __name__ == '__main__':
    clean_up_directories()
    cars = get_input()
    print("cars", cars)
    process_data(cars)

from car_data.car_list import all_cars

if __name__ == '__main__':
    # point 1

    for car in all_cars:
        car['id'] = id(car)
    # point 2
    slow_cars = [car for car in all_cars if car["hp"] < 120]
    print("Slow cars are : ", slow_cars)

    fast_cars = [car1 for car1 in all_cars if 120 < car1["hp"] < 180]
    print("Fast cars are: ", fast_cars)

    sport_cars = [car2 for car2 in all_cars if car2["hp"] >= 180]
    print("Sport cars are: ", sport_cars)

    cheap_cars = [car3 for car3 in all_cars if car3["price"] < 1000]
    print("Cars with price low are: ", cheap_cars)

    medium_cars = [car4 for car4 in all_cars if 1000 <= car4["price"] < 5000]
    print("Cars with medium price are: ", medium_cars)

    expensive_cars = [car5 for car5 in all_cars if car5["price"] >= 5000]
    print("Cars with price high are: ", expensive_cars)

    # point 3
    import os
    import csv
    import json

    data = {}

    with open('input.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            BRAND = row["BRAND"]
            if BRAND not in data:
                data[BRAND] = []
            data[BRAND].append(row)


            def is_slow_car(car6):
                return int(car6["HORSEPOWER"]) < 120


            def is_fast_car(car7):
                return 120 < int(car7["HORSEPOWER"]) < 180


            def is_sport_car(car8):
                return int(car8["HORSEPOWER"]) >= 180


            def is_cheap_car(car9):
                return int(car9["PRICE"]) < 1000


            def is_medium_car(car10):
                return 1000 < int(car10["PRICE"] < 5000)


            def is_expensive_car(car11):
                return int(car11["PRICE"]) >= 5000

    output_folder = 'output_data'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


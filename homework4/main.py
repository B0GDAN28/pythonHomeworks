if __name__ == '__main__':
    # point 1
    # all_cars = [{"brand": "Opel", "Model": "Astra H", "hp": 150, "price": 2500},
    #             {"brand": "Dacia", "Model": "Logan I", "hp": 100, "price": 900},
    #             {"brand": "Bmw", "Model": "520d", "hp": 190, "price": 15000},
    #             {"brand": "Ford", "Model": "Focus II", "hp": 130, "price": 2000},
    #             {"brand": "Dacia", "Model": "Sandero", "hp": 90, "price": 700},
    #             {"brand": "Volkswagen", "Model": "Passat", "hp": 170, "price": 5000},
    #             {"brand": "Skoda", "Model": "Superb", "hp": 150, "price": 4000},
    #             {"brand": "Audi", "Model": "A6", "hp": 190, "price": 13000},
    #             {"brand": "Mercedes-Benz", "Model": "E-klasse", "hp": 190, "price": 17000},
    #             {"brand": "Skoda", "Model": "Octavia", "hp": 140, "price": 3000}]
    # for car in all_cars:
    #     car['id'] = id(car)
    # # point 2
    # slow_cars = filter(lambda car0: car0["hp"] < 120, all_cars)
    # slow_cars = list(slow_cars)
    # print("Slow cars are : ", slow_cars)
    #
    # fast_cars = filter(lambda car1: 120 < car1["hp"] < 180, all_cars)
    # fast_cars = list(fast_cars)
    # print("Fast cars are: ", fast_cars)
    #
    # sport_cars = filter(lambda car2: car2["hp"] >= 180, all_cars)
    # sport_cars = list(sport_cars)
    # print("Sport cars are: ", sport_cars)
    #
    # cheap_cars = filter(lambda car3: car3["price"] < 1000, all_cars)
    # cheap_cars = list(cheap_cars)
    # print("Cars with price low are: ", cheap_cars)
    #
    # medium_cars = filter(lambda car4: 1000 <= car4["price"] < 5000, all_cars)
    # medium_cars = list(medium_cars)
    # print("Cars with medium price are: ", medium_cars)
    #
    # expensive_cars = price_high = filter(lambda car5: car5["price"] >= 5000, all_cars)
    # expensive_cars = list(expensive_cars)
    # print("Cars with price high are: ", expensive_cars)

    # point 3
    import csv

    with open('input.csv', newline='') as input_csv:
        reader = csv.reader(input_csv, delimiter=',', quotechar='"')
        for row in reader:
            print(', '.join(row))


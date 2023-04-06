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
    import csv

    filename = "input.csv"
    header = ["BRAND", "MODEL", "HP", "PRICE"]
    data = [
        ["OPEL", "ASTRA H", 150, 2500],
        ["DACIA", "LOGAN I", 100, 900],
        ["BMW", "520D", 190, 15000],
        ["FORD", "FOCUS II", 130, 2000],
        ["DACIA", "SANDERO I", 90, 700],
        ["VOLKSWAGEN", "PASSAT B6", 170, 5000],
        ["SKODA", "SUPERB I", 150, 4000],
        ["AUDI", "A6 C7", 190, 13000],
        ["MERCEDES-BENZ", "E-KLASSE W212", 204, 170000],
        ["SKODA", "OCTAVIA II", 140, 3000]

    ]
    with open(filename, 'w', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
        csvwriter.writerows(data)

from car_data.car_list import all_cars

if __name__ == '__main__':
    # program1

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

    #  program2

    file = open("input.csv", "r")


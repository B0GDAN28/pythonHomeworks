from car_data import car_list

all_cars = [
    {"brand": "Opel", "Model": "Astra H", "hp": 150, "price": 2500},
    {"brand": "Dacia", "Model": "Logan I", "hp": 100, "price": 900},
    {"brand": "Bmw", "Model": "520d", "hp": 190, "price": 15000},
    {"brand": "Ford", "Model": "Focus II", "hp": 130, "price": 2000},
    {"brand": "Dacia", "Model": "Sandero", "hp": 90, "price": 700},
    {"brand": "Volkswagen", "Model": "Passat", "hp": 170, "price": 5000},
    {"brand": "Skoda", "Model": "Superb", "hp": 150, "price": 4000},
    {"brand": "Audi", "Model": "A6", "hp": 190, "price": 13000},
    {"brand": "Mercedes-Benz", "Model": "E-klasse", "hp": 190, "price": 17000},
    {"brand": "Skoda", "Model": "Octavia", "hp": 140, "price": 3000}
]
if __name__ == '__main__':
    def slow_cars(all_cars):
        hp_low = filter(lambda car: car["hp"] < 120, all_cars)
        hp_low = list(hp_low)
        print(hp_low)


    slow_cars(all_cars)


    def fast_cars(all_cars):
        hp_medium = filter(lambda car: car["hp"] > 120 and car["hp"] < 180, all_cars)
        hp_medium = list(hp_medium)
        print(hp_medium)


    fast_cars(all_cars)


    def sport_cars(all_cars):
        hp_high = filter(lambda car: car["hp"] >= 180, all_cars)
        hp_high = list(hp_high)
        print(hp_high)


    sport_cars(all_cars)


    def cheap_cars(all_cars):
        price_low = filter(lambda car: car["price"] < 1000, all_cars)
        price_low = list(price_low)
        print(price_low)


    cheap_cars(all_cars)


    def medium_cars(all_cars):
        price_medium = filter(lambda car: car["price"] >= 1000 and car["price"] < 5000 , all_cars)
        price_medium = list(price_medium)
        print(price_medium)


    medium_cars(all_cars)


    def expensive_cars(all_cars):
        price_high = filter(lambda car: car["price"] >= 5000 , all_cars)
        price_high = list(price_high)
        print(price_high)


    expensive_cars(all_cars)





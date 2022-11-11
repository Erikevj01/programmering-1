from datetime import date

car_register = {
    "toyotaBZ4X": {
        "brand": "Toyota",
        "model": "Corolla",
        "price": 96_000,
        "year": 2012,
        "month": 8,
        "new": False,
        "km": 163_000
    },
    "pugeot408": {
        "brand": "Pugeot",
        "model": "408",
        "price": 330_000,
        "year": 2019,
        "month": 1,
        "new": False,
        "km": 40_000
    },
    "audiRS3": {
        "brand": "Audi",
        "model": "RS3",
        "price": 473_000,
        "year": 2022,
        "month": 2,
        "new": True,
        "km": 0
    },
}

NEW_CAR_REGISTRATION_FEE = 8745
RENT_CAR_PERCENTAGE = 0.4
RENT_NEW_CAR__FEE = 1000


def calculate_total_price(car):
    used_car_fee = 0
    new_car_fee = 10783
    car_age = 2022 - car_register[car]['year']

    if -1 < car_age < 4:
        used_car_fee = 6681
    if 3 < car_age < 12:
        used_car_fee = 4034
    if 11 < car_age < 30:
        used_car_fee = 1729
    if car_age > 30:
        used_car_fee = 0

    if car_register[car]['new']:
        total_price = car_register[car]['price'] + new_car_fee
        print(f"The total price for this {car_register[car]['brand']} {car_register[car]['model']} is {total_price}")
    else:
        total_price = car_register[car]['price'] + used_car_fee
        print(f"The total price for this {car_register[car]['brand']} {car_register[car]['model']} is {total_price}")


calculate_total_price("toyotaBZ4X")
calculate_total_price("pugeot408")
calculate_total_price("audiRS3")
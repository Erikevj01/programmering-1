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


def print_car_information(car):
    print(f"Brand: {car_register[car]['brand']}\n"
          f"Model: {car_register[car]['model']}\n"
          f"Price: {car_register[car]['price']}\n"
          f"Manufactured: {date(car_register[car]['month'], car_register[car]['year'])}\n"
          f"Condition: Yes\n"
          f"Km: {car_register[car]['km']}\n")


print_car_information(car_register["toyotaBZ4X"])
print_car_information(car_register["pugeot408"])
print_car_information(car_register["audiRS3"])

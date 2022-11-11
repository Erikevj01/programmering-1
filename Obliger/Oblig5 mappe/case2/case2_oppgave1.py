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


def print_car_information(car):
    manufacture_date = date(car_register[car]['year'], car_register[car]['month'], 1)
    print(f"Brand: {car_register[car]['brand']}\n"
          f"Model: {car_register[car]['model']}\n"
          f"Price: {car_register[car]['price']}\n"
          f"Manufactured: {manufacture_date.year}-{manufacture_date.month}")
    if car_register[car]['new']:
        print("Condition: New\n")
    else:
        print("Condition: Used\n")


print_car_information("toyotaBZ4X")
print_car_information("pugeot408")
print_car_information("audiRS3")

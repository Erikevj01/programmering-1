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


def next_eu_control(car):
    manufacture_date = date(car_register[car]['year'], car_register[car]['month'], 1)
    date_today = date.today()
    car_age = date_today.year - manufacture_date.year
    if car_age % 2 == 0:
        euc_year = date_today.year
        print(f"Next EU-control for the "
              f"{car_register[car]['brand']}{car_register[car]['model']}"
              f"is {euc_year}-{manufacture_date.month}-{manufacture_date.day}")
    else:
        euc_year = date_today.year + 1
        print(f"Next EU-control for the "
              f"{car_register[car]['brand']}{car_register[car]['model']}"
              f"is {euc_year}-{manufacture_date.month}-{manufacture_date.day}")



next_eu_control("toyotaBZ4X")
next_eu_control("pugeot408")
next_eu_control("pugeot408")
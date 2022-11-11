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


def rent_car_monthly_price(car):
    car_fee = 0
    if car_register[car]['new']:
        car_fee = RENT_NEW_CAR__FEE
    car_rent = car_register[car]['price'] * RENT_CAR_PERCENTAGE / 12 + car_fee
    print(f"If you want to rent the {car_register[car]['brand']} {car_register[car]['model']} "
          f"the monthly fee will be {round(car_rent, 2)}")


rent_car_monthly_price("toyotaBZ4X")
rent_car_monthly_price("pugeot408")
rent_car_monthly_price("audiRS3")
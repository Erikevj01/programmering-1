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


def create_car(car_register, brand, model, price, year, month, new, km):
    car_details = {
        "brand": brand,
        "model": model,
        "price": price,
        "year": year,
        "month": month,
        "new": new,
        "km": km
    }
    car_register[f"{(brand.lower())}{model.lower()}"] = car_details


create_car(car_register, "Volvo", "V90", 850_000, 2021, 12, True, 0)
print(car_register)

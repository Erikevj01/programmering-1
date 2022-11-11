class Car:
    def __init__(self, brand, model, price, year, month, new, km):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.month = month
        self.new = new
        self.km = km

    def print_car_information(car):
        return
    # Denne funksjonen er relevant fordi den kan benyttes til å vise frem informasjon om gitt bil til brukeren
    def create_car(car_register, brand, model, price, year, month, new, km):
        return
    # Denne funksjonen er essensiell for å kunne ha flere biler enten til salg eller leie.
    def get_car_age(car):
        return
    # Jeg tenker denne funksjonen er relevant fordi brukeren kan ha interesse i hvor gammel gitt bil er.
    def next_eu_control(car):
        return
    # Brukeren har mest sannsynlig stor interesse i når de må ha neste EU kontrol.
    # Derfor synes jeg denne er relevant når det gjelder informasjon om gitt bil til brukeren.
    def rent_car_monthly_price(car):
        return
    # Denne er funksjonen er relevant siden den finner månedlig leie ved gitt bil.
    # Dette er essensielt til utleie av biler.
    def calculate_total_price(car):
        return
    # Ved slag av biler er denne funksjonen relevant for å finne prisen av kjøpet.


car1 = Car("Toyota", "Corolla", 96_000, 2012, 8, False, 163_000)
car2 = Car("Pugeot", "408", 330_000, 2019, 1, False, 40_000)
car3 = Car("Audi", "RS3", 473_000, 2022, 2, True, 0)


print(car1.brand, car1.model)
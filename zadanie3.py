class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Dzielnica:{self.area},  Pomieszczenia:{self.rooms}, Cena: {self.price}, adres: {self.address}"


Property1 = Property("Centrum", "15", "13400", "Katowicka 12")


class House(Property):
    def __init__(self, area, rooms, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"Rozmiar działki: {self.plot}, Dzielnica:{self.area}, Pomieszczenia: {self.rooms} Cena{self.price}, Adres {self.address}"


class Flat(Property):
    def __init__(self, floor: int, area, rooms, price, address):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Piętro {self.floor}, Dzielnica: {self.area} Cena: {self.price}, Adres: {self.address}"


House1 = House("Katowice", "12", "12330", "Koszutka", 123)
Flat1 = Flat(3, "Kraków", "2", "210002", "Studencka 7")
print(House1)
print(Flat1)

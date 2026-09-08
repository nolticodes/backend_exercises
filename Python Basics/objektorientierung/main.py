class Säugetier:
    def __init__(self, farbe, rasse, name):
            self.farbe = farbe
            self.rasse = rasse
            self.name = name

    def vorstellen(self):
            print(f"Ich bin {self.name}")
    
    def essen(self):
        pass

    def laufen(self):
        pass


class Katze(Säugetier):
    def miauen():
        pass


class Hund(Säugetier):
    def bellen(self):
        pass


dog1 = Hund("braun", "dackel", "Zeus")
dog2 = Hund("grün", "dackel", "Emma")

dog1.vorstellen()


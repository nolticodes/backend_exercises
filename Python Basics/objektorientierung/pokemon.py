class Pokemon:

    def __init__(self, name, level):
        self.name = name
        self.level = 1
        self.__lebenspunkte = 42
        self.vorstellen()

    def __str__(self):
        return f"Name: {self.name} \nLebenspunkte: {self.__lebenspunkte} \nLevel: {self.level} "

    def __gt__(self, other):
        return self.level > other.level

    def vorstellen(self):
        print(f"Moin ich bin {self.name}")

    def zeige_lebenspunkte(self):
        return self.__lebenspunkte

    def level_up(self):
        self.level += 1

    def attack(self, other, schaden):
        other.__lebenspunkte -= schaden

if __name__ == "__main__":
    bisasam = Pokemon("Bisasam", 15)
    pikachu = Pokemon("Pikachu", 25)
    bisasam.level_up()
    print(bisasam.zeige_lebenspunkte())

    bisasam.attack(pikachu, 10)

    print(pikachu)                  # ruft die __str__ funktion auf

    print(pikachu > bisasam)        # true 

    

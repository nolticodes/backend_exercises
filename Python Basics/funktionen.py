# args
# variable Anzhal an parametern können übergeben werden
def addieren(*summanden):
    print(sum(summanden))
    
addieren(1, 2, 3)   # 6
addieren(2, 4)      # 6
addieren(1, 2, 10)  # 13

def addieren2(startzahl, *summanden):
    print(f"Deine Startzhal: {startzahl}")
    print(sum(summanden))



#kwargs (keyword args)
# dictionaries werden ausgegeben 
# Übergabeparameter müssen nicht in einer festen Reihenfolge angegeben werden
# Es knnen auch parameter übergeben werden, die erstmal nicht verwendet werden
# Parameter die nicht übergeben werden, führen nicht zu fehler. Es wird none ausgegeben, oder es wird ein default wert definiert
def kwargs_test(**test):
    print(test)

kwargs_test(a=2, b=3, c=6)      # {"a": 2, "b": 3 "c": 6}

def teilnehmer(**daten):
    vorname = daten.get("vorname")
    nachname = daten.get("nachname")
    alter = daten.get("alter", 18)
    print(f"{vorname} {nachname}; {alter}")

teilnehmer(vorname="Florian", nachname="bla")               # Florian bla; 18
teilnehmer(vorname="Florian", nachname="bla", alter=29)     # Floroan bla, 29


#scoping
level = 0
def level_up():
    global level    # globale variable wird in den scope der funktion geholt
    level += 1


#Module entwicklen und einbauen
# wird mit den befehel und dem namen der zu importierenden datei in der ziel datei eingebunden (hier: modul_einbinden.py)
def addieren(a, b):
    return a + b

def subtrahieren(a, b):
    return a - b


# if__name__=="__main__"
# wird verwendet wenn module importier werden, um nur die funktionen zu erhalten und das ausführen von methoden von importiereten methoden zu blockieren.
# so können tests in den zu importierenden mpdulen erhalten bleiben

if __name__=="__main__":
    addieren(1, 6)          # würde nicht in einer datei in diese datei imporitert ist ausgeführt werden


# input-funktion

name = input("Gib deinen Namen ein: ")

print(f"Hallo {name}")


# exec Funktionen


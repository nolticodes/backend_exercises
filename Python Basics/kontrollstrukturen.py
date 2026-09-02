# muss im Terminal ausgeführt werden

# # if-Anweisungen
passwort = input("Gib dein passwort ein: ")

if passwort == "123":
    print("Korrekt")
else: 
    print("Falsch")


# if elif else Anweisung
note = input("Gib eine Note ein: ")

if note == "1":
    print("Sehr gut")
elif note == "2":
    print("gut")
elif note == "2":
    print("befriedigend") 
elif note == "4":
    print("ausreichend")
elif note == "5":
    print("mangelhaft")
elif note == "6":
    print("ungenügend")
else:
    print("note ungültig")


# match case Anweisung
note = input("Gib eine Note ein: ")

match note:
    case "1":
        print("Sehr gut")
    case "2":
        print("gut")
    case "2":
        print("befriedigend") 
    case "4":
        print("ausreichend")
    case "5":
        print("mangelhaft")
    case "6":
        print("ungenügend")
    case _:
        print("note ungültig")


# for Schleifen
passwörter = ["abc", "123", "abc123", "123abc"]

for passwort in passwörter:
    print(passwort)
    if len(passwort) > 5:
        break
# Ausgabe: Wird bis einschließlich "abc123" ausgegeben, da break erst danache erfolgt


# while Schleifen
x = 25
runde = 1

while x > 0 :
    print(f"Runde: {runde}")
    runde += 1 
    x -= 1


# Walross operator
teilnehmerliste = []

while (teilnehmer := input("Nenne den Teilnehmer (X): ")) != "X":
    teilnehmerliste.append(teilnehmer)

print(teilnehmerliste)
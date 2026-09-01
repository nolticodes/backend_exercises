# Code Ausführen in Terminal:
# mit cmd + a ganzen Text markieren oder nur den gewünschten bereich markeiren
# mit shift + enter code ausführen und in Terminal anzeigen

# formatierter String
# benötigen ein f im code
name = "Denis"
age = 29

print(f"Ich bin {name} und {age} alt")


# Variablen lassen sich in python in einer Zeile definieren
name2, age2 = "Melodi", 26

print(f"Ich bin {name2} und {age2} alt")


# Variablen können den Datentypn wechseln 
age3 = 18
age3 = "Achtzehn"

# Methode um sich alle keywords in python ausgeben zu lassen (dürfen icht als variablen namen verwendet werden)
import keyword

print(keyword)


# ÜBUNGSAUFGABEN
# 1 Welche der folgenden Variablennamen sind in Python gültig und welche nicht?

# python123 -> gültig
# 0815 -> ungültig
# __python__ -> gültig
# Fehler -> gültig
# false -> gültig
# hallo_welt -> gültig
# True -> ungültig
# nicht-richtig -> ungültig
# tmp.2 -> ungültig
# yield -> ungültig


#2 Gegeben seien die folgenden Variablen
# Vertausche die Werte der beiden Variablen vorname und nachname, damit der Vor- und Nachname richtig zugewiesen ist

vorname = "Mustermann"
nachname = "Max"

vorname, nachname = nachname, vorname 


#3 Gegeben sei das folgende Python-Programm
a = 42
b = a
c = a
a = 10
b = c

#Welche Werte werden in den folgenden Zeilen ausgegeben?
# print(a) -> 10
# print(b) -> 42
# print(c) -> 42


#4 Gegeben sei das folgende Python-Programm:
vorname = "Misa"
nachname = "Amani"
geschlecht = "weiblich"
tag = 22
monat = "September"
jahr = "1998"

print(f"""Mein Name ist {vorname} {nachname}.\nIch bin {geschlecht} und wurde am {tag}. {monat} {jahr} geboren.""")
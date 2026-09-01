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


# ÜBUNGSAUFGABEN VARIABLEN
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
print(a) #-> 10
print(b) #-> 42
print(c) #-> 42


#4 Gegeben sei das folgende Python-Programm:
vorname = "Misa"
nachname = "Amani"
geschlecht = "weiblich"
tag = 22
monat = "September"
jahr = "1998"

print(f"""Mein Name ist {vorname} {nachname}.\nIch bin {geschlecht} und wurde am {tag}. {monat} {jahr} geboren.""")


# DATENTYPEN
name = "Denis"      # string
age = 29            # integer (ganze Zahlen!)
highage = 100_000   # integer (ganzzahl die zu besseren lesbarkeit mit underscore getrennt werden können)
weight = 85.3       # float (kommazahlen)
antwort = True      # true oder false, wichtig Großschreiben!

# Datentypen ausgeben lassen mit type()
print(type(name))

# Datentypen umwandeln
str()               # Wert in String umwandeln 
int()               # Wert in Interger umwandeln
float()             # Wert in Float umwandeln


# ÜBUNGSAUFGABEN DATENTYPEN
# Welche der folgenden Umwandlungen sind möglich und was ist das Ergebnis?
int(42.5)           # 42
float(-1)           # -1.0
str(0.5)            # "0.5"
bool(0.001)         # true
str("False")        # "False"
int(False)          # 0
float("10")         # 10.0
bool('0')           # true -> weil ein nicht leerer string übergeben würde. Wenn int übergeben wprden wäre wäre ergbns false
int("False")        # ungültig
float("True")       # ungültig
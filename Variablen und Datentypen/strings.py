# Strings definieren

name = "Denis"
name2 = 'Denis'
"""
    Diese dienen zur Dokumentation
    """


# Einzelne Zeichen aus einem String auslesen

string = "Denis"

print(len(name))    # Ausgabe: 5
print(name[2])      # Ausgabe: n
print(name[-2])     # Ausgabe: i


# String Slicing

sliceString = "Melodi"
print(sliceString[0:3])     # Ausgabe: Mel -> 3 ist die erste Stelle in Kette die nicht berücksichtigt wird
print(sliceString[0:4])     # Ausgabe: Melo
print(sliceString[:4])      # Ausgabe: Melo -> Wenn bei 0 gestartet wird, dann kann diese weggelassen werden 
print(sliceString[3:])      # Ausgabe: odi -> Wenn es bis zum Ende des Strings gehen soll, kann die Zahl weggelassen werden

# ÜBUNG SLICING

# Was wird von dem folgenden Programm ausgegeben?
a = "Buchhaltung"
b = "Python ist toll!"
print(a[5])                 # a     
print(b[-1])                # ! 
print(a[:4])                # Buch
print(b[11:16])             # toll!
print(a[-100:100])          # Buchhaltung
print(a[-5])                # l
print(a[-12])               # error
print(a[4:8])               # halt

# Schneide mithilfe von Slicing aus dem String
wort = "Maximilian"

"""
Max                         # print(wort[0:3])
Maxi                        # print(wort[0:4])
im                          # print(wort[3:5])
mili                        # print(wort[4:8]) oder print(wort[-6:-3])
ian                         # print(wort[-3:-1]) oder print(wort[7:])
"""       


# Strings konkatenieren

vorname = "Denis"
nachname = "Nolting"

print(vorname + " " + nachname)
print(3*vorname)                    # Minus und getielt funktuioniren nicht mit Strings

# ÜBUNG STRINGS KONKATENIEREN
# Was wird von dem folgenden Programm ausgegeben? Gib, wenn es zu einem Fehler kommt, an, welcher Fehler auftritt und warum.

a = "Developer"
b = "Akademie"
c = '.'
d = "com"

print(a + b)            # DeveloperAkademie
print(a + b + c + d)    # DeveloperAkademie.com
print(a + b - b)        # error
print(5 * c)            # .....
print(3d)               # error
print(a + d)            # Developercom
print(a + b + d)        # DeveloperAkademiecom
print(d**2)             # error
print(2 * (c + d))      # .com.com
print(3 * c + 2 * d)    # ...comcom


# String Methoden
# String emthode anzeigen lassen mit "print(dir(str))"

name = "Denis"
name.zfill(10)          # Ausgabe: "00000Denis" -> setzt fünf null vor den string da 5 Zeichen minus 10 gleich 5 ist
"Denis123".upper()      # Aushabe: "DENIS123"
"Denis123".lower()      # Ausgabe: "denis123"
"DENIS".capitalize()    # Ausgabe: "Denis"
"denis".isupper()       # Ausgabe: false
"DENis".isupper()       # Ausgabe: false -> PRüft ALLE Buchstaben 
"denis".islower()       # Ausgabe: true
"denis123".isnumeric()  # Ausgabe: false
"123".isnumeric()       # Ausgabe: true
"denis123".isalpha()    # Ausgabe: false
"denis".isalpha()       # Ausgabe: true

"Denis; Melodi; Hasi; Schmausi".split(';')      # Ausgabe: ['Denis', 'Melodi', ...]
"Denis\nMelodi\nHasi\nSchmausi"                 # Ausgabe: Die Namen werden untereinander gelistet
"Denis\nMelodi\nHasi\nSchmausi".splitlines()    # Ausgabe: Die Namen werden an Zeilenumbrüchen getrennt und eine liste gepackt (eine Zeile)
"   Denis    ".strip()                          # Ausgabe: "Denis"
"    Den   is    ".strip()                      # Ausgabe: "Den   nis" -> nur am Anfagn und ende
"    Den   is    ".replace(" ", "")             # Ausgabe: "Denis" -> Alle Leerzeichen werden durch nichts ("") ersetzt
"Denis".replace("Denis", "Melodi")              # Ausgabe: "Melodi"
"Mausiii".count("i")                            # Ausgabe: 3
"MAUSIII".count("i")                            # Ausgabe: 0
"Mausiii".index("a")                            # Ausgabe: 1 (index)
"Mausiiii".find("i")                            # Ausgabe: 4
"Mausi".find("D")                               # Ausgabe -1 -> Wenn kein Wert gefunden, kann index() nicht
"a" in "Mausi"                                  # Ausgabe: true
"d" in "Mausi"                                  # Ausgabe: false


# ÜBUNG STING METHODEN
# Was wird von dem folgenden Programm ausgegeben?

passwort1 = "abc123"
passwort2 = "Pass Wort"
passwort3 = "u1tr4g3h31m "

print(passwort1.upper())                # "ABC123"
print(passwort2.lower())                # "pass wort"
print(passwort3.islower())              # true
print(passwort2.isupper())              # false
print(passwort1.zfill(8))               # "00abc123"
print(passwort2.strip())                # "Pass Wort"
print(len(passwort3))                   # 12    
print(passwort1.isalpha())              # false
print(passwort1[3:].isnumeric())        # true
print("a;b;c;d;e".split(';'))           # ['a', 'b', 'c', 'd', 'e']
print("01.23.45.67.89".split(';'))      # "01.23.45.67.89"
print(passwort2.replace("Pass",'.'))    # ". Wort"
print(passwort3.count('3'))             # 2
print(passwort2.count('s'))             # 2
print(passwort3.find(2+2))              # error (int können nicht gefunden werden)
print(passwort1.index("4"))             # false

# Verwende passende String-Methoden, um die vorgegebenen Strings in die umzuwandeln, die als Kommentar vorgegeben sind
"passw0r7".replace("pass", "PASS")  # PASSw0r7        
"Anime".zfill(11)                   # 000000Anime
"florian".capitalize()              # Florian
"Kaguya".lower()                    # kaguya
"0123456789"[::-1]                  # 9876543210
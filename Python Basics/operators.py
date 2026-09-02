# Arithmetische Operatoren 

print(12 + 10)      # 22
print(12 - 10)      # 2
print(12 * 2)       # 24
print(12 / 2)       # 6.0
print(12 / 5)       # 2.4
print(12 // 2)      # 6
print(12 // 5)      # 2
print(12 % 5)       # 2   gibt es den Restwert zurück (12 - 10 = 2)
print(10**2)        # 100


# Übung arithmetische Operatoren 
print(12 * 12)                  # 144
print(2.5 + 3.5)                # 6.0
print(20 / 5)                   # 4.0
print(15 - 3 * 5)               # 0
print(8 + 10//4)                # 10
print(8 + 10/4)                 # 10.5
print(20 / (5 - 4))             # 20.0
print(4 * 2.5 / 4)              # 2.5
print(1//2 - 3//4)              # 0
print((12 % 5) * (5 % 12))      # 10
print(2**3)                     # 8
print(4**(8 - 5))               # 64
print(2**(8 // 2))              # 16
print(5**2 * 3)                 # 75
print((8 - 5)**(27 // 9))       # 27
print("apfel" + "baum")         # apfelbaum
print(5 * ("a" + "b"))          # ababababab
print("x" * 2**3)               # xxxxxxxx
print(12 % 5)                   # 2
print(42 % 43)                  # 42
print(2**10 % 2)                # 0
print(5 * 4 * 3 * 2 * 1.0)      # 120.0
print(0 * "Florian")            # 
print("xyz" * (12 % 5))         # xyzxyz


# Inkrement und Dekrement Operator
i = 0
i += 1      # das gleiche wie i = i + 1
i -= 1      # das gleiche wie i = i - 1
i /= 2      # das gleiche wie i = i / 2

a = 5
a **=2      # das gleiche wie a = a**2

b = 10
b %= 3      # das gleiche wie b = b % 3


# Vergleichsoperatoren
# gibt true oder false aus

12 < 15         # true   
20 <= 22        # true
56 == 56        # true
17 != 42        # true
99 > 33         # true
18 >= 18        # true

"denis" <= "denis"  # true, die länger der Strigns wird verglichen 


# Logische Operatoren 
True and True       # true
True and False      # false
False and True      # false
False and False     # false

True or True        # true
True or False       # true
False or True       # true
False or False      # false

# Entweder oder (beides geht nicht)
True ^ True         # False
True ^ False        # True
False ^ True        # True
False ^ False       # False

# Übung logische Operatoren 
# Welche Wahrheitswerte kommen bei den folgenden logischen Ausdrücken heraus?

True and False and True or False        # false       
not False or not True                   # true    
True and (False or not False)           # true    
not (not False ^ True or not False)     # false   
True and False ^ True and False         # false

# Worin besteht der Unterschied zwischen den beiden Operatoren ^ und or?
# or: entweder oder oder beides
# ^: entweder oder, aber nicht beides

# Welche Wahrheitswerte kommen als Ergebnis heraus?
2 < 3 and not 2 > 5                     # True
not True ^ False or 3 == 2 + 1          # True
not not not 2 % 5 == 7 % 5              # False
True and False ^ True and False         # False
True ^ False ^ 0 ^ 1 ^ (2 > 3)          # 0
# Számológép
print("Számológép")

szam1 = input("Kérek egy számot: ")
while not szam1.isnumeric():
    print("Rossz érték!!")
    szam1 = input("Kérek egy számot: ")
szam1 = int(szam1)

muvelet = input("Kérem a műveleti jelet! (+, -, /, *)")
while muvelet not in ["+", "-", "/", "*"]:
    print("Nem érvényes a műveleti jel!!")
    muvelet = input("Kérem a műveleti jelet! (+, -, /, *)")

szam2 = input("Kérek egy másik számot: ")
while not szam2.isnumeric():
    print("Rossz érték!!")
    szam2 = input("Kérek egy másik számot: ")
szam2 = int(szam2)

eredmeny = 0
if muvelet == "+":
    eredmeny = szam1 + szam2

elif muvelet == "-":
    eredmeny = szam1 - szam2

elif muvelet == "/":
    eredmeny = szam1 / szam2

elif muvelet == "*":
    eredmeny = szam1 * szam2

print(str(szam1).rjust(50))
print(muvelet, end="")
print(str(szam2).rjust(49))
print("".rjust(50, "_"))
print(str(eredmeny).rjust(50))

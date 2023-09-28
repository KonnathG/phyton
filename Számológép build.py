# Számológép
def adatkeres(tipus):
    valasz = ""
    if tipus == "sz":
        valasz = input("Kérek egy számot: ")
        while not valasz.isnumeric():
            print("Rossz érték!!")
            valasz = input("Kérek egy számot: ")
        valasz = int(valasz)
    elif tipus == "m":
        valasz = input("Kérem a műveleti jelet! (+, -, /, %, *)")
        while valasz not in ["+", "-", "/", "%", "*"]:
            print("Nem érvényes a műveleti jel!!")
            valasz = input("Kérem a műveleti jelet! (+, -, /, %, *)")
    return valasz


def szamolas():
    eredmenye = 0
    if muvelet == "+":
        eredmenye = szam1 + szam2

    elif muvelet == "-":
        eredmenye = szam1 - szam2

    elif muvelet == "/":
        eredmenye = szam1 / szam2

    elif muvelet == "%":
        eredmenye = szam1 % szam2

    elif muvelet == "*":
        eredmenye = szam1 * szam2
    return eredmenye


# Prog eleje
print("Számológép")
szam1 = adatkeres("sz")
muvelet = adatkeres("m")
szam2 = adatkeres("sz")
eredmeny = szamolas()

print(str(szam1).rjust(50))
print(muvelet, end="")
print(str(szam2).rjust(49))
print("".rjust(50, "_"))
print(str(eredmeny).rjust(50))

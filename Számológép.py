# számológép


def adatkeres(tipus):
    valasz = ""
    if tipus == "sz":
        valasz = input("Kérek egy számot")
        while(valasz.isnumeric()) is False:
            print("Rossz érték!")
            valasz = input("Kérek egy számot")
        valasz = int(valasz)
    elif tipus == "m":
        valasz = input("Milyen művelete legyen(+,-,*,/): ")
        while valasz not in ["+", "-", "*", "/"]:
            print("A megadott műveleti jelek közül válasszon!")
            valasz = input("Milyen művelete legyen(+,-,*,/): ")
    return valasz


def szamolas():
    eredmenye = 0
    if muvelet == "+":
        eredmenye = (szam1 + szam2)

    elif muvelet == "-":
        eredmenye = (szam1 - szam2)

    elif muvelet == "*":
        eredmenye = (szam1 * szam2)

    elif muvelet == "/":
        eredmenye = (szam1 / szam2)

    return eredmenye


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
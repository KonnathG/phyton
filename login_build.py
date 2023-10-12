# Beléptető rendszer
def regisztracio():
    sikeres = True
    felhasznalonev()
    jelszo_bekerese()
    i = 0
    while not jelszo_ellenorzese():
        print("Nem egyezik a két jelszó")
        i += 1
        if i > 3:
            sikeres = False
            break

    return sikeres


def felhasznalonev():
    felhasznalo_email = input("Kérem adja meg az email címét: ")
    while " " in felhasznalo_email or "@" not in felhasznalo_email or "." not in felhasznalo_email:
        felhasznalo_email = input("Nem megfelelő az email!\nKérem adja meg az emailcímét: ")


def jelszo_bekerese():
    felhasznalo_jelszava = input("Kérek egy jelszót (1,a,A, min 8 karakter)")
    rossz_jelszo = True
    while rossz_jelszo:
        rossz_jelszo=False
        if len(felhasznalo_jelszava) < 8:
            rossz_jelszo = True

        van = 0
        for i in range(len(felhasznalo_jelszava)):
            if felhasznalo_jelszava[i].isnumeric():
                van += 1
            if van == 0:
                rossz_jelszo = True
        van = 0

        for i in range(len(felhasznalo_jelszava)):
            if felhasznalo_jelszava[i].isupper():
                van += 1
            if van == 0:
                rossz_jelszo = True

        van = 0
        for i in range(len(felhasznalo_jelszava)):
            if felhasznalo_jelszava[i].islower():
                van += 1
            if van == 0:
                rossz_jelszo = True

        if rossz_jelszo == True:
            felhasznalo_jelszava = input("Kérek egy jelszót (1,a,A, min 8 karakter)")
        else:
            rossz_jelszo = False
            print(f"Ez a jelszavad: {felhasznalo_jelszava}")


def jelszo_ellenorzese():
        ok_jelszo = True
        return ok_jelszo


def beleptetes():
    pass


# Innen indul a program
felhasznalo_email = ""
felhasznalo_jelszava = ""
"felhasznalonev()"
jelszo_bekerese()

"""if regisztracio():
    beleptetes()
else:
    print("Sikertelen regisztráció!")
"""

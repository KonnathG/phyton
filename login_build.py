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
    felhasznalo_jelszava = input("Kérek egy jelszót (1,a,A, min 8 karakter): ")
    ok_pw = True
    while ok_pw:
        if len(felhasznalo_jelszava) < 8:
            ok_pw = False

        van = 0
        for i in range(len(felhasznalo_jelszava)):
            if felhasznalo_jelszava[i].isnumeric():
                van += 1
        if van == 0:
            ok_pw = False

        van = 0
        for i in range(len(felhasznalo_jelszava)):
            if felhasznalo_jelszava[i].isupper():
                van += 1
        if van == 0:
            ok_pw = False

        van = 0
        for i in range(len(felhasznalo_jelszava)):
            if felhasznalo_jelszava[i].islower():
                van += 1
        if van == 0:
            ok_pw = False

        if not ok_pw:
            felhasznalo_jelszava = input("Nem megfelelő a megadott jelszó!\nKérek egy jelszót (1,a,A, min 8 karakter): ")
            ok_pw = True
        else:
            ok_pw = False
            print(f"Ez a jelszavad: {felhasznalo_jelszava}")


def jelszo_ellenorzese():
        ok_pw = True
        return ok_pw


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

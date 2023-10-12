# Beléptető rendszer
def regisztracio():
    sikeres = True
    felhasznalo_email = felhasznalonev()
    felhasznalo_jelszava = jelszo_bekerese()
    if not jelszo_ellenorzese(felhasznalo_jelszava, 3):
        sikeres = False

    if sikeres:
        with open("jelszo.txt", "a", encoding="utf-8") as fajl:
            fajl.write(felhasznalo_email + ";" + felhasznalo_jelszava + "\n")
    return sikeres


def felhasznalonev():
    felhasznalo_email = input("Kérem adja meg az email címét: ")
    while " " in felhasznalo_email or "@" not in felhasznalo_email or "." not in felhasznalo_email:
        felhasznalo_email = input("Nem megfelelő az email!\nKérem adja meg az emailcímét: ")
    return felhasznalo_email


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
    return felhasznalo_jelszava


def jelszo_ellenorzese(felhasznalo_jelszo, proba):
    i = 1
    jelszo2 = input("Kérem ismét a jelszót: ")
    while jelszo2 != felhasznalo_jelszo and i < proba:
        jelszo2 = input("Kérem ismét a jelszót: ")
        i += 1
    if jelszo2 == felhasznalo_jelszo:
        ok_pw = True
    else:
        ok_pw = False
    return ok_pw


def beleptetes():
    pass


# Innen indul a program
if regisztracio():
    print("Sikerült a regisztráció, most beléptetjük")
    beleptetes()
else:
    print("Sikertelen regisztráció!\nPróbálja újra")

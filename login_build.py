# Beléptető rendszer
def regisztracio():
    sikeres = True
    felhasznalo_email = felhasznalonev()
    felhasznalo_jelszava = jelszo_bekerese()
    if not jelszo_ellenorzese(felhasznalo_jelszava, 3, "Kérem ismét a jelszót: "):
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


def jelszo_ellenorzese(felhasznalo_jelszo, proba, uzenet):
    i = 1
    jelszo2 = input(uzenet)
    while jelszo2 != felhasznalo_jelszo and i < proba:
        jelszo2 = input(uzenet)
        i += 1
    if jelszo2 == felhasznalo_jelszo:
        ok_pw = True
    else:
        ok_pw = False
    return ok_pw


def felhasznalo_ellenorzese(felhasznalo):
    jelszo = ""
    with open("jelszo.txt", "r", encoding="UTF-8") as fajl:
        for sor in fajl:
            lista = sor.strip("\n")
            user = lista.split(";")
            if user[0] == felhasznalo:
                jelszo = user[1]
    return jelszo


def beleptetes():
    ok_belepes = True
    jelszo = felhasznalo_ellenorzese(felhasznalonev())
    if jelszo == "":
        print("Nincs ilyen felhasználó, kérem regisztrálja!")
        ok_belepes = False
    else:
        if not jelszo_ellenorzese(jelszo, 3, "Kérem adja meg a jelszavát: "):
            print("Téves jelszó!")
            ok_belepes = False
    return ok_belepes


# Innen indul a program
if __name__ == "__main__":
    if regisztracio():
        print("Sikerült a regisztráció, most beléptetjük")
        if beleptetes():
            print("Sikeres bejelentkezés!")
        else:
            print("Sikertelen belépés, próbálja újra!")
    else:
        print("Sikertelen regisztráció!\nPróbálja újra")

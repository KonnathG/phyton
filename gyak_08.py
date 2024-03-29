from tkinter import *
from tkinter import messagebox
import gyak_09
from gyak_10 import *


def beleptetes_ablak():
    def ok_gomb_feldolgozasa():
        if ab_jelszokereses(felh_nev.get()) == felh_jelszo.get():
            messagebox.showinfo("Belépés", "Üdv a fedélzeten!")
        else:
            messagebox.showerror("Belépés", "Hibás bejelentkezési adat!")
        belepes.destroy()

    def reg_gomb_feldolgozasa():
        belepes.destroy()
        pass

    belepes = Toplevel()

    belepes.title("Felhasználó beléptetése")

    felh_nev_cimke = Label(belepes, text="A felhasználó neve (email):")
    felh_jelszo_cimke = Label(belepes, text="Jelszó:")

    fhsz = StringVar()
    fhsz.set("")
    felh_nev = Entry(belepes, textvariable=fhsz, width=30)
    fjsz = StringVar()
    fjsz.set("")
    felh_jelszo = Entry(belepes, textvariable=fjsz, width=20, show="*")

    gomb_ok = Button(belepes, text="OK", command=ok_gomb_feldolgozasa)
    gomb_reg = Button(belepes, text="Regisztráció", command=reg_gomb_feldolgozasa)

    felh_nev_cimke.grid(row=0, column=0, padx=20, pady=20, sticky=E)
    felh_jelszo_cimke.grid(row=1, column=0, padx=20, sticky=E)
    felh_nev.grid(row=0, column=1, padx=20, sticky=W)
    felh_jelszo.grid(row=1, column=1, padx=20, sticky=W)
    gomb_ok.grid(row=2, column=0, pady=20)
    gomb_reg.grid(row=2, column=1)

    belepes.mainloop()


def regisztracio_ablak():
    def ok_gomb_kezelese():
        if reg_jelszo.get() != reg_jelszo2.get():
            messagebox.showerror("Hiba", "Nem egyforma a két jelszó!")
            regisztracio.attributes('-topmost', True)
            regisztracio.attributes('-topmost', False)
        elif fhsz.jelszo_ellenorzese(reg_jelszo.get()):
            messagebox.showerror("Hiba", "A jelszó nem felel meg a kritériumoknak!")
            regisztracio.attributes('-topmost', True)
            regisztracio.attributes('-topmost', False)
        elif " " in fhemail.get() or "@" not in fhemail.get() or "." not in fhemail.get():
            messagebox.showerror("Hiba", "Nem megfelelő az email formátum!")
            regisztracio.attributes('-topmost', True)
            regisztracio.attributes('-topmost', False)
        else:
            ab_regisztracio(fhemail.get(), reg_jelszo.get())
            regisztracio.destroy()

    def jelszo_gen_gomb_kezelese():
        fhsz.jelszo_generalasa(10, True, True, True)
        jsz0 = fhsz.jelszo
        jsz.set(jsz0)
        jsz2.set(jsz0)

    regisztracio = Toplevel()
    regisztracio.title("Regisztráció")

    reg_felh_cimke = Label(regisztracio, text="A felhasználó neve (email):")

    reg_jelszo_cimke = Label(regisztracio, text="Jelszó:")
    reg_jelszo2_cimke = Label(regisztracio, text="Jelszó ismét:")

    fhemail = StringVar()
    fhemail.set("")
    reg_felh = Entry(regisztracio, textvariable=fhemail, width=30)
    jsz = StringVar()
    jsz.set("")
    jsz2 = StringVar()
    jsz2.set("")
    reg_jelszo = Entry(regisztracio, textvariable=jsz, width=20, show="*")
    reg_jelszo2 = Entry(regisztracio, textvariable=jsz2, width=20, show="*")

    gomb_ok = Button(regisztracio, text="OK", command=ok_gomb_kezelese)
    jelszo_gen_gomb = Button(regisztracio, text="Jelszó generálása", command=jelszo_gen_gomb_kezelese)

    reg_felh_cimke.grid(row=0, column=0)
    reg_jelszo_cimke.grid(row=1, column=0)
    reg_jelszo2_cimke.grid(row=2, column=0)
    reg_felh.grid(row=0, column=1)
    reg_jelszo.grid(row=1, column=1)
    reg_jelszo2.grid(row=2, column=1)
    gomb_ok.grid(row=3, column=0)
    jelszo_gen_gomb.grid(row=1, column=2)

    regisztracio.mainloop()


# főprogram
app = Tk()
app.title("Dolgozók nyilvántartása")
app.minsize(300, 200)
fhsz = gyak_09.Felhasznalo("", "")

ab_letrehozas()

menusor = Menu(app)

hozzaferes = Menu(menusor)
hozzaferes.add_command(label="Belépés", command=beleptetes_ablak)
hozzaferes.add_command(label="Regisztráció", command=regisztracio_ablak)
hozzaferes.add_command(label="Kilépés", command=app.destroy)
menusor.add_cascade(label="Hozzáférés", menu=hozzaferes)

dolgozok = Menu(menusor)
dolgozok.add_command(label="Lista", command=app.destroy)
dolgozok.add_command(label="Névjegy", command=app.destroy)
menusor.add_cascade(label="Dolgozók", menu=dolgozok)

app.config(menu=menusor)
app.mainloop()
ab_lezaras()

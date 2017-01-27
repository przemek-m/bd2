import datetime
from random import randint
from faker import Factory
# fake = Factory.create('pl_PL')
fake = Factory.create()

N_Autor = 5000
N_Dzial = 100
N_Pozycja = 100000
N_Seria = 1000
N_Wolumen = N_Pozycja * 4
N_Czytelnik = 10000
N_Wypozyczenie = 100000
N_Rezerwacja = 100


def autor():
    with open("autor.sql", "w") as f:
        f.write("SET autocommit=0;\n")
        for i in range(1, N_Autor+1):
            f.write(
                "insert into Autor (ID, nazwa) values ({}, \'{}\');\n".format(
                    i, fake.name()
                ))
            if i % 900 == 0:
                f.write("COMMIT;\n")
        f.write("COMMIT;\n")


def dzial():
    with open("dzial.sql", "w") as f:
        f.write("SET autocommit=0;\n")
        for i in range(1, N_Dzial+1):
            f.write(
                "insert into Dzial (ID, nazwa) values ({}, \'{}\');\n".format(
                    i, fake.last_name_male()
                ))
        f.write("COMMIT;\n")


def pozycja():
    with open("pozycja.sql", "w") as f:
        f.write("SET autocommit=0;\n")
        for i in range(1, N_Pozycja+1):
            f.write(
                "insert into Pozycja (ID, nazwa, okladka, Dzial_ID) values ({}, \'{}\', \'{}.jpg\', {});\n".format(
                    i, fake.text(max_nb_chars=35), i, randint(1, N_Dzial)
                ))
            if i % 900 == 0:
                f.write("COMMIT;\n")
        f.write("COMMIT;\n")


def pozycja_autorzy():
    with open("pozycja_autorzy.sql", "w") as f:
        f.write("SET autocommit=0;\n")
        for i in range(1, N_Pozycja+1):
            f.write(
                "insert into Pozycja_Autorzy (Pozycja_ID, Autor_ID) values ({}, {});\n".format(
                    i, randint(1, N_Autor)
                ))
            if i % 900 == 0:
                f.write("COMMIT;\n")
        f.write("COMMIT;\n")


def seria():
    with open("seria.sql", "w") as f:
        f.write("SET autocommit=0;\n")
        for i in range(1, N_Seria+1):
            f.write(
                "insert into Seria (ID, nazwa) values ({}, \'{}\');\n".format(
                    i, fake.last_name_male()
                ))
        f.write("COMMIT;\n")


def wolumen():
    isbn = [fake.ean13() for i in range(0, N_Pozycja+1)]
    with open("wolumen.sql", "w") as f:
        f.write("SET autocommit=0;\n")
        for i in range(1, N_Pozycja):
            f.write(
                "insert into Wolumen (ID, Pozycja_ID, Seria_ID, rodzaj_numeru, numer) values ({}, {}, {}, \'{}\', \'{}\');\n".format(
                    i, i, randint(1, N_Seria), "ISBN", isbn[i]
                ))
            if i % 900 == 0:
                f.write("COMMIT;\n")
        f.write("COMMIT;\n")
        for i in range(N_Pozycja, N_Wolumen+1):
            poz = randint(1, N_Pozycja)
            f.write(
                "insert into Wolumen (ID, Pozycja_ID, Seria_ID, rodzaj_numeru, numer) values ({}, {}, {}, \'{}\', \'{}\');\n".format(
                    i, poz, randint(1, N_Seria), "ISBN", isbn[poz]
                ))
            if i % 900 == 0:
                f.write("COMMIT;\n")
        f.write("COMMIT;\n")


def czytelnik():
    with open("czytelnik.sql", "w") as f:
        f.write("SET autocommit=0;\n")
        for i in range(1, N_Czytelnik+1):
            f.write(
                "insert into Czytelnik (ID, imie, nazwisko, email, haslo) values ({}, \'{}\', \'{}\', \'{}\', \'{}\');\n".format(
                    i, fake.first_name(), fake.last_name(), fake.email(), fake.word()
                ))
            if i % 900 == 0:
                f.write("COMMIT;\n")
        f.write("COMMIT;\n")


def dane_czytelnika():
    with open("dane_czytelnika.sql", "w") as f:
        f.write("SET autocommit=0;\n")
        for i in range(1, N_Czytelnik+1):
            f.write(
                "insert into DaneCzytelnika (kod_pocztowy, miasto, ulica, numer_budynku, numer_lokalu, Czytelnik_ID) values (\'{}\', \'{}\', \'{}\', {}, {}, {});\n".format(
                    fake.postcode(), fake.city(), fake.street_name(), randint(1,100), randint(1,100), i
                ))
            if i % 900 == 0:
                f.write("COMMIT;\n")
        f.write("COMMIT;\n")


def wypozyczenie():
    with open("wypozyczenie.sql", "w") as f:
        f.write("SET autocommit=0;\n")
        for i in range(1, N_Wypozyczenie+1):
            date = datetime.datetime.now() - datetime.timedelta(days=randint(0,700))
            due_date = date + datetime.timedelta(days=30)
            return_date = date + datetime.timedelta(days=randint(1,60))
            f.write(
                "insert into Wypozyczenie (ID, data, termin_zwrotu, data_zwrotu, Wolumen_ID, Czytelnik_ID) values ({}, \'{}\', \'{}\', \'{}\', {}, {});\n".format(
                    i, date, due_date, return_date, randint(1,N_Wolumen), randint(1,N_Czytelnik), i
                ))
            if i % 900 == 0:
                f.write("COMMIT;\n")
        f.write("COMMIT;\n")


def rezerwacja():
    with open("rezerwacja.sql", "w") as f:
        f.write("SET autocommit=0;\n")
        for i in range(1, N_Rezerwacja+1):
            date = datetime.datetime.now() + datetime.timedelta(days=randint(-20,0))
            due_date = date + datetime.timedelta(days=30)
            f.write(
                "insert into Rezerwacja (ID, data_utworzenia, data_waznosci, Wolumen_ID, Czytelnik_ID) values ({}, \'{}\', \'{}\', {}, {});\n".format(
                    i, date, due_date, randint(1,N_Wolumen), randint(1,N_Czytelnik)
                ))
            if i % 900 == 0:
                f.write("COMMIT;\n")
        f.write("COMMIT;\n")


def generate():
    autor()
    dzial()
    pozycja()
    pozycja_autorzy()
    seria()
    wolumen()
    czytelnik()
    dane_czytelnika()
    wypozyczenie()
    rezerwacja()


generate()

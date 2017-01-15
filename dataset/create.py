import datetime
from random import randint
from faker import Factory
fake = Factory.create('pl_PL')


N_Autor = 5
N_Dzial = 20
N_Pozycja = 100
N_Seria = 10
N_Wolumen = N_Pozycja * 3
N_Czytelnik = 10
N_Wypozyczenie = 100


def autor():
    with open("autor.sql", "w") as f:
        for i in range(1, N_Autor+1):
            f.write(
                "insert into Autor (ID, nazwa) values ({}, \'{}\');\n".format(
                    i, fake.name()
                ))


def dzial():
    with open("dzial.sql", "w") as f:
        for i in range(1, N_Dzial+1):
            f.write(
                "insert into Dzial (ID, nazwa) values ({}, \'{}\');\n".format(
                    i, fake.last_name_male()
                ))


def pozycja():
    with open("pozycja.sql", "w") as f:
        for i in range(1, N_Pozycja+1):
            f.write(
                "insert into Pozycja (ID, nazwa, okladka, Dzial_ID) values ({}, \'{}\', \'{}.jpg\', {});\n".format(
                    i, fake.text(max_nb_chars=35), i, randint(1, N_Dzial)
                ))


def pozycja_autorzy():
    with open("pozycja_autorzy.sql", "w") as f:
        for i in range(1, N_Pozycja+1):
            f.write(
                "insert into Pozycja_Autorzy (Pozycja_ID, Autor_ID) values ({}, {});\n".format(
                    i, randint(1, N_Autor)
                ))


def seria():
    with open("seria.sql", "w") as f:
        for i in range(1, N_Seria+1):
            f.write(
                "insert into Seria (ID, nazwa) values ({}, \'{}\');\n".format(
                    i, fake.last_name_male()
                ))


def wolumen():
    with open("wolumen.sql", "w") as f:
        for i in range(1, N_Pozycja):
            f.write(
                "insert into Wolumen (ID, Pozycja_ID, Seria_ID) values ({}, {}, {});\n".format(
                    i, i, randint(1, N_Seria)
                ))
        for i in range(N_Pozycja, N_Wolumen+1):
            f.write(
                "insert into Wolumen (ID, Pozycja_ID, Seria_ID) values ({}, {}, {});\n".format(
                    i, randint(1, N_Pozycja), randint(1, N_Seria)
                ))


def czytelnik():
    with open("czytelnik.sql", "w") as f:
        for i in range(1, N_Czytelnik+1):
            f.write(
                "insert into Czytelnik (ID, imie, nazwisko, email, haslo) values ({}, \'{}\', \'{}\', \'{}\', \'{}\');\n".format(
                    i, fake.first_name(), fake.last_name(), fake.email(), fake.word()
                ))


def dane_czytelnika():
    with open("dane_czytelnika.sql", "w") as f:
        for i in range(1, N_Czytelnik+1):
            f.write(
                "insert into DaneCzytelnika (kod_pocztowy, miasto, ulica, numer_budynku, numer_lokalu, Czytelnik_ID) values (\'{}\', \'{}\', \'{}\', {}, {}, {});\n".format(
                    fake.postcode(), fake.city(), fake.street_name(), randint(1,100), randint(1,100), i
                ))


def wypozyczenie():
    with open("wypozyczenie.sql", "w") as f:
        for i in range(1, N_Wypozyczenie+1):
            date = datetime.datetime.now() - datetime.timedelta(days=randint(0,700))
            due_date = date + datetime.timedelta(days=30)
            return_date = date + datetime.timedelta(days=randint(1,60))
            f.write(
                "insert into Wypozyczenie (ID, data, termin_zwrotu, data_zwrotu, Wolumen_ID, Czytelnik_ID) values ({}, \'{}\', \'{}\', \'{}\', {}, {});\n".format(
                    i, date, due_date, return_date, randint(1,N_Wolumen+1), randint(1,N_Czytelnik+1), i
                ))


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


generate()

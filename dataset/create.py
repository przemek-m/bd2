from random import randint
from faker import Faker
fake = Faker()


N_Autor = 5
N_Dzial = 20
N_Pozycja = 100
N_Seria = 10
N_Wolumen = N_Pozycja * 3


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


def generate():
    autor()
    dzial()
    pozycja()
    pozycja_autorzy()
    seria()
    wolumen()

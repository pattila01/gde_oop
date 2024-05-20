#######################################
############ SZALLODA.PY ##############
#######################################

# szoba.py fájlból származtatjuk az EgyagyasSzoba és KetagyasSzoba osztályokat:
from szoba import EgyagyasSzoba, KetagyasSzoba

# Szalloda osztály deklarálása:
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    # függvényt deklarálunk a szobák hozzáadásához
    def szoba_hozzaadas(self, szoba):
        self.szobak.append(szoba)

    # függvényt deklarálunk a szobák listázásához
    def szobak_listazasa(self):
        for szoba in self.szobak:
            print(szoba.info())
#######################################
############ FOGLALAS.PY ##############
#######################################

# szalloda.py fájlból származtatjuk a Szalloda osztályt:
from szalloda import Szalloda

# Foglalas osztály deklarálása:
class Foglalas:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = []

    # függvényt deklarálunk a szobák foglalásához
    def szoba_foglalas(self, szobaszam, datum):
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                self.foglalasok.append({"szobaszam": szobaszam, "datum": datum, "ar": szoba.ar})
                return szoba.ar
        return None

    # függvényt deklarálunk a foglalás lemondásához
    def foglalas_lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas["szobaszam"] == szobaszam and foglalas["datum"] == datum:
                self.foglalasok.remove(foglalas)
                return True
        return False

    # függvényt deklarálunk a foglalások kilistázásához
    def foglalasok_listazasa(self):
        for foglalas in self.foglalasok:
            print(f"Szobaszám: {foglalas['szobaszam']}, Dátum: {foglalas['datum']}, Ár: {foglalas['ar']}")

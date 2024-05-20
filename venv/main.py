"""
Author: Puizl Attila Zoltán - SK4MX8 - Mérnökinformatikus - alapképzés
Date: 2024-05-21
Description: Ez a program egy szállodai szobafoglalási rendszert valósít meg Pythonban
             Boga Áron Zsombor tanár úr részére.
             A rendszer képes szobák kezelésére, foglalások létrehozására, lemondására
             és listázására. A felhasználói interfész lehetővé teszi a felhasználók
             számára, hogy különböző műveleteket hajtsanak végre.
             Köszönöm a megtekintést.
"""

#######################################
############## MAIN.PY ################
#######################################

# minden szükséges osztály deklarálása a különböző fájlokból:
from szalloda import Szalloda
from szoba import EgyagyasSzoba, KetagyasSzoba
from foglalas import Foglalas

# menü függvény létrehozása:
def menu():
    print()
    print("--- GDE FOGLALÁSI RENDSZER ---")
    print()
    print("1 -> Szoba foglalása")
    print("2 -> Foglalás lemondása")
    print("3 -> Foglalások listázása")
    print("4 -> Kilépés")

# alapfóggvénnyel feltöltjük a programot a demóadatokkal:
def main():
    szalloda = Szalloda("GDE Szálloda")
    szalloda.szoba_hozzaadas(EgyagyasSzoba(10000, 101))
    szalloda.szoba_hozzaadas(KetagyasSzoba(15000, 102))
    szalloda.szoba_hozzaadas(KetagyasSzoba(15000, 103))

    foglalas = Foglalas(szalloda)
    foglalas.szoba_foglalas(101, "2024-05-01")
    foglalas.szoba_foglalas(102, "2024-05-02")
    foglalas.szoba_foglalas(103, "2024-05-03")
    foglalas.szoba_foglalas(101, "2024-05-04")
    foglalas.szoba_foglalas(102, "2024-05-05")

    # várjuk az interakciót a felhasználótól:
    while True:
        menu()
        print()
        valasztas = input("Választás: ")

        # feltételes utasítás a különböző menüpontok kezeléséhez:
        if valasztas == "1":
            szobaszam = int(input("Szobaszám: "))
            datum = input("Dátum (YYYY-MM-DD): ")
            ar = foglalas.szoba_foglalas(szobaszam, datum)
            if ar:
                print(f"Foglalás sikeres! Ár: {ar} Ft")
            else:
                print("A szoba nem elérhető a megadott dátumon.")
        elif valasztas == "2":
            szobaszam = int(input("Szobaszám: "))
            datum = input("Dátum (YYYY-MM-DD): ")
            sikeres = foglalas.foglalas_lemondas(szobaszam, datum)
            if sikeres:
                print("Foglalás lemondva.")
            else:
                print("Nincs ilyen foglalás.")
        elif valasztas == "3":
            foglalas.foglalasok_listazasa()
        elif valasztas == "4":
            break
        else:
            print("Érvénytelen választás.")

# main függvény meghívása, ha a script közvetlenül futtatva van:
if __name__ == "__main__":
    main()
#######################################
############# SZOBA.PY ################
#######################################

# absztrakt osztályok létrehozásához szükséges csomagok implementálása:
from abc import ABC, abstractmethod

# Szoba osztály deklarálása:
class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def info(self):
        pass

# EgyagyasSzoba osztály deklarálása, mely örökli a Szoba osztályt:
class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(ar, szobaszam)

    def info(self):
        return f"Egyágyas szoba - Szobaszám: {self.szobaszam}, Ár: {self.ar}"

# KetagyasSzoba osztály deklarálása, mely örökli a Szoba osztályt:
class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(ar, szobaszam)

    def info(self):
        return f"Kétágyas szoba - Szobaszám: {self.szobaszam}, Ár: {self.ar}"
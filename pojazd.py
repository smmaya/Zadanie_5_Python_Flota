from operacje import *


class Pojazd:
    def __init__(self, marka: str, model: str, rejestracja: str, rocznik: int, przebieg: int):
        self.marka = marka
        self.model = model
        self.rejestracja = rejestracja
        self.rocznik = rocznik
        self.przebieg = przebieg
        self.lista_przegladow = list()
        self.lista_serwisow_oleju = list()
        self.lista_serwisow_opon = list()
        self.lista_tankowan = list()
        self.lista_wypadkow = list()

    def zmien_przebieg(self, tankowanie: Tankowanie):
        nowy_przebieg = int(input('Podaj stan licznika: '))
        stary_przebieg = self.przebieg
        ilosc_paliwa = tankowanie.zatankowano
        spalanie = (ilosc_paliwa / (nowy_przebieg - stary_przebieg)) * 100
        print(f'Srednie spalanie: {spalanie}')
        self.przebieg = nowy_przebieg
        tankowanie.zmien_spalanie(spalanie)


    def __str__(self):
        return f'{self.marka} {self.model} {self.rejestracja} {self.rocznik} {self.przebieg}'

    def wypisz_operacje(self, choice: int):
        if choice == 1:
            operacja: Operacja
            for operacja in self.lista_przegladow:
                operacja.wypisz_operacje()
        elif choice == 2:
            operacja: Operacja
            for operacja in self.lista_serwisow_oleju:
                operacja.wypisz_operacje()
        elif choice == 3:
            operacja: Operacja
            for operacja in self.lista_serwisow_opon:
                operacja.wypisz_operacje()
        elif choice == 4:
            operacja: Operacja
            for operacja in self.lista_tankowan:
                operacja.wypisz_operacje()
        elif choice == 5:
            operacja: Operacja
            for operacja in self.lista_wypadkow:
                operacja.wypisz_operacje()
        elif choice == 6:
            operacja: Operacja
            for operacja in self.lista_przegladow:
                operacja.wypisz_operacje()
            for operacja in self.lista_serwisow_oleju:
                operacja.wypisz_operacje()
            for operacja in self.lista_serwisow_opon:
                operacja.wypisz_operacje()
            for operacja in self.lista_tankowan:
                operacja.wypisz_operacje()
            for operacja in self.lista_wypadkow:
                operacja.wypisz_operacje()
        elif choice == 0:
            return
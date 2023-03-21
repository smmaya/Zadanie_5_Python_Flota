"""
Sławomir Majchrzak | 60473 - INiN_6_PR2.1
Program do zarządzania flotą pojazdów w firmie.

Główne funkcjonalności:
- Klasy:
    - Pojazd:

"""

from operacje import *

# Lista pojazdow
pojazdy = list()


class Pojazd:
    def __init__(self, marka: str, model: str, rejestracja: str, rocznik: int):
        self.marka = marka
        self.model = model
        self.rejestracja = rejestracja
        self.rocznik = rocznik
        self.lista_przegladow = list()
        self.lista_serwisow_oleju = list()
        self.lista_serwisow_opon = list()
        self.lista_tankowan = list()
        self.lista_wypadkow = list()

    def dodaj_operacje(self):
        print('- Dodaj operacje -')
        print('1 - Dodaj przegląd techiczny')
        print('2 - Dodaj serwis oleju')
        print('3 - Dodaj serwis opon')
        print('4 - Dodaj tankowanie')
        print('5 - Dodaj wypadek')
        print('0 - Wyjdź')
        choice = int(input('Co chcesz zrobić? Podaj numer z menu: '))
        if choice == 1:
            self.lista_przegladow.append(PrzegladTechniczny.stworz_operacje())
        elif choice == 2:
            self.lista_serwisow_oleju.append(SerwisOleju.stworz_operacje())
        elif choice == 3:
            self.lista_serwisow_opon.append(SerwisOpon.stworz_operacje())
        elif choice == 4:
            self.lista_tankowan.append(Tankowanie.stworz_operacje())
        elif choice == 5:
            self.lista_wypadkow.append(Wypadek.stworz_operacje())
        elif choice == 0:
            return

    def __str__(self):
        return f'{self.marka} {self.model} {self.rejestracja} {self.rocznik}'

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


def dodaj_pojazd():
    print('\n~ Dodawanie pojazdu ~')
    marka = input('Podaj markę pojazdu: ')
    model = input('Podaj model: ')
    rejestracja = input('Numer rejestracyjny (bez spacji): ')
    rocznik = int(input('Rok produkcji: '))
    pojazd = Pojazd(marka, model, rejestracja, rocznik)
    print(f'\nDodano pojazd: {pojazd}')
    pojazdy.append(pojazd)


def usun_pojazd():
    print('\n~ Usuwanie pojazdu ~')
    id_pojazdu = int(input('Który pojazd chcesz usunąć? Podaj id: '))
    try:
        pojazdy.pop(id_pojazdu)
        print('\nPojazd pomyślnie usunięto z bazy.')
        print('-' * 64)
    except IndexError:
        print('\nNie ma takiego id w bazie.')


def wybierz_pojazd() -> Pojazd:
    while True:
        id_pojazdu = int(input('Podaj id pojazdu: '))
        if len(pojazdy) > id_pojazdu > 0:
            return pojazdy[id_pojazdu]
        else:
            print('Nie ma takiego id w bazie.')


def main():
    pojazdy.append(Pojazd('Audi', 'A4', "GD999LR", 2015))
    pojazdy.append(Pojazd('Peugeot', '406', "WA123CS", 2019))
    pojazdy.append(Pojazd('Peugeot', '406', "ST245DF", 2020))
    pojazdy.append(Pojazd('Nissan', 'Pathfinder', "GT987PK", 2013))
    pojazdy.append(Pojazd('Nissan', 'Patrol', "GS942LY", 2005))
    pojazdy.append(Pojazd('Ford', 'Transit', "GA223RR", 2023))
    pojazdy.append(Pojazd('Opel', 'Movano', "RT259LL", 2006))
    pojazdy.append(Pojazd('Ford', 'Transit', "PO463AS", 2003))
    print('''
                      ⠀⠀ ⣀⣤⣤⣴⣶⣶⣿⠿⠿⠿⢿⣶⣶⣤⣀⣀⣀⣠⣤⣤⣦⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠈⢿⡏⠉⢻⣿⣿⣿⣿⣿⡆⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠋⠀⠀⠀⣴⣶⡄⠀⠀⢰⣿⠀⠀⠀⠘⣷⡀⠀⢹⣿⣿⣿⣿⣿⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣇⣀⣤⣤⣤⣾⣿⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⡆
        ⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
        ⠀⣰⠋⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣁⣀⣠⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
        ⣰⣷⣦⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⣿⣿⣿⣿⣿⣿⣿⠁⠈⠙⢿⣿⣿⣿⣿⠀⣿⠀
        ⣿⣿⣿⣿⣿⣷⡀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠘⣿⣿⣿⣿⠀⣿⠀
        ⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⣀⣀⣀⣀⣀⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣿⣿⣿⣿⣀⣿⠀
        ⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢀⣼⣿⠛⠛⠛⠛⠃⠀
        ⠀⠈⠙⠻⢿⣿⣿⣿⠿⠟⠛⠛⠛⠛⠛⠉⠉⠉⠉⠉⠀⠈⠻⣿⣿⣿⣷⣶⣶⣿⡿⠁⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
                      ''', end='')
    print('Witaj w programie zarządzania flotą!')
    while True:
        try:
            print('-' * 40)
            print('--- MENU GŁÓWNE --- Wybierz z menu 0-9: ')
            print('-' * 40)
            print('1 - Wypisz wszystkie pojazdy')
            print('2 - Dodaj pojazd')
            print('3 - Usuń pojazd')
            print('4 -> Tankowanie')
            print('5 -> Przegląd techniczny')
            print('6 -> Serwis opon')
            print('7 -> Serwis oleju')
            print('8 -> Wypadek')
            print('9 -> Wszystkie operacje pojazdu')
            print('0 - >> Wyjdź <<')
            print('-' * 30)
            choice = int(input('Co chcesz zrobić? Podaj numer z menu: '))
            if choice == 1:
                pojazd: Pojazd
                for pojazd in pojazdy:
                    print(pojazd)
            elif choice == 2:
                dodaj_pojazd()
            elif choice == 3:
                usun_pojazd()
            elif choice == 4:
                print('- Stacja paliw -')
                print('1 - Zatankuj')
                print('2 - Wypisz wszystkie tankowania')
                print('0 - Wróć do głównego menu')
                print('-' * 15)
                t_menu = int(input('Tankowanie - podaj numer z menu: '))
                if t_menu == 1:
                    wybierz_pojazd().lista_tankowan.append(Tankowanie.stworz_operacje())
                elif t_menu == 2:
                    wybierz_pojazd().wypisz_operacje(4)
                elif t_menu == 0:
                    continue
            elif choice == 5:
                print('- Stacja kontroli -')
                print('1 - Dodaj przegląd')
                print('2 - Wypisz wszystkie przeglądy')
                print('0 - Wróć do głównego menu')
                print('-' * 15)
                p_menu = int(input('Przeglądy - podaj numer z menu: '))
                if p_menu == 1:
                    wybierz_pojazd().lista_przegladow.append(PrzegladTechniczny.stworz_operacje())
                if p_menu == 2:
                    wybierz_pojazd().wypisz_operacje(1)
                if p_menu == 0:
                    continue
            elif choice == 6:
                print('- Warsztat opon -')
                print('1 - Dodaj serwis opon')
                print('2 - Wypisz wszystkie serwisy opon')
                print('0 - Wróć do głównego menu')
                print('-' * 15)
                op_menu = int(input('Opony - podaj numer z menu: '))
                if op_menu == 1:
                    wybierz_pojazd().lista_serwisow_opon.append(SerwisOpon.stworz_operacje())
                if op_menu == 2:
                    wybierz_pojazd().wypisz_operacje(3)
                if op_menu == 0:
                    continue
            elif choice == 7:
                print('- Warsztat oleju -')
                print('1 - Dodaj serwis oleju')
                print('2 - Wypisz wszystkie serwisy oleju')
                print('0 - Wróć do głównego menu')
                print('-' * 15)
                ol_menu = int(input('Tankowanie - podaj numer z menu: '))
                if ol_menu == 1:
                    wybierz_pojazd().lista_serwisow_oleju.append(SerwisOleju.stworz_operacje())
                if ol_menu == 2:
                    wybierz_pojazd().wypisz_operacje(2)
                if ol_menu == 0:
                    continue
            elif choice == 8:
                print('- Kolizje i stłuczki -')
                print('1 - Dodaj wypadek')
                print('2 - Wypisz wszystkie wypadki')
                print('0 - Wróć do głównego menu')
                print('-' * 15)
                w_menu = int(input('Wypadki - podaj numer z menu: '))
                if w_menu == 1:
                    wybierz_pojazd().lista_wypadkow.append(Wypadek.stworz_operacje())
                if w_menu == 2:
                    wybierz_pojazd().wypisz_operacje(5)
                if w_menu == 0:
                    continue
            elif choice == 9:
                wybierz_pojazd().wypisz_operacje(6)
            elif choice == 0:
                print('Do zobaczenia!')
                return

        except ValueError:
            print('~~~~~')
            print('Błąd, wybrano literę lub inny znak. Wybierz 0-9: ')
            print('~~~~~')
            continue
        if choice not in range(0, 10):
            print('~~~~~')
            print('Zły wybór, numer poza zasięgiem menu. Wybierz 0-9: ')
            print('~~~~~')
            continue


if __name__ == '__main__':
    main()

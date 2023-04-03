"""
Sławomir Majchrzak | 60473 - INiN_6_PR2.1

Program do zarządzania flotą pojazdów w firmie.

Główne funkcjonalności:
    - Wypisanie floty
    - Dodawanie pojazdów
    - Usuwanie pojazdów
    - kontrole techniczne z obliczeniem dni do następnej kontroli
    - Zarządzanie tankowaniami z obliczeniem średniego spalania
    - Serwis opon
    - Serwis oleju
    - Rejestr wypadków
"""
from pojazd import *

# Lista pojazdow
pojazdy = list()


def dodaj_pojazd():
    print('\n~ Dodawanie pojazdu ~')
    marka = input('Podaj markę pojazdu: ')
    model = input('Podaj model: ')
    rejestracja = input('Numer rejestracyjny (bez spacji): ')
    rocznik = int(input('Rok produkcji: '))
    przebieg = int(input('Podaj przebieg: '))
    pojazd = Pojazd(marka, model, rejestracja, rocznik, przebieg)
    print(f'\nDodano pojazd: ')
    pojazdy.append(pojazd)
    print(pojazdy.index(pojazd) + 1, pojazd)


def usun_pojazd():
    print('\n~ Usuwanie pojazdu ~')
    id_pojazdu = int(input('Który pojazd chcesz usunąć? Podaj id: '))
    try:
        pojazdy.pop(id_pojazdu - 1)
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
    pojazdy.append(Pojazd('Audi', 'A4', "GD999LR", 2015, 10000))
    pojazdy.append(Pojazd('Peugeot', '406', "WA123CS", 2019, 20000))
    pojazdy.append(Pojazd('Peugeot', '406', "ST245DF", 2020, 30000))
    pojazdy.append(Pojazd('Nissan', 'Pathfinder', "GT987PK", 2013, 40000))
    pojazdy.append(Pojazd('Nissan', 'Patrol', "GS942LY", 2005, 50000))
    pojazdy.append(Pojazd('Ford', 'Transit', "GA223RR", 2023, 60000))
    pojazdy.append(Pojazd('Opel', 'Astra', "RT259LL", 2006, 70000))
    pojazdy.append(Pojazd('Ford', 'Transit', "PO463AS", 2003, 80000))
    pojazd: Pojazd = pojazdy[1]
    pojazd.lista_serwisow_oleju.append(SerwisOleju(date(2023, 1, 12)))
    pojazd.lista_przegladow.append(PrzegladTechniczny(date(2023, 2, 9), False))
    pojazd.lista_tankowan.append(Tankowanie(date(2023, 3, 10), 34))
    pojazd.lista_serwisow_opon.append(SerwisOpon(date(2023, 1, 2)))
    pojazd.lista_wypadkow.append(Wypadek(date(2023, 2, 18), 0, 0))

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
                    print(pojazdy.index(pojazd) + 1, pojazd)
            elif choice == 2:
                dodaj_pojazd()
            elif choice == 3:
                usun_pojazd()
            elif choice == 4:
                print('- Stacja paliw -')
                print('1 - Zatankuj')
                print('2 - Wypisz tankowania pojazdu')
                print('0 - Wróć do głównego menu')
                print('-' * 15)
                t_menu = int(input('Tankowanie - podaj numer z menu: '))
                if t_menu == 1:
                    poj = wybierz_pojazd()
                    tankowanie = Tankowanie.stworz_operacje()
                    poj.zmien_przebieg(tankowanie)
                    poj.lista_tankowan.append(tankowanie)
                elif t_menu == 2:
                    wybierz_pojazd().wypisz_operacje(4)
                elif t_menu == 0:
                    continue
            elif choice == 5:
                print('- Stacja kontroli -')
                print('1 - Dodaj przegląd')
                print('2 - Wypisz przeglądy pojazdu')
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
                print('2 - Wypisz serwisy opon pojazdu')
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
                print('2 - Wypisz serwisy oleju pojazdu')
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
                print('2 - Wypisz wypadki pojazdu')
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

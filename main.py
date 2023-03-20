"""
Sławomir Majchrzak | 60473 - INiN_6_PR2.1
Program do zarządzania flotą pojazdów w firmie.

Główne funkcjonalności:
- Tworzenie bazy danych sqlite3 'flota.db'
- Klasy:
    - Pojazd (+11 metod):
        Metody:
            - Dodanie serii pojazdów w celu wypełnienia bazy
            - Dodanie pojazdu
            - Usunięcie pojazdu
            - Ręczna zmiana przebiegu
            - Wypisanie floty
            - Wypisanie danych pojazdu
            - Dodanie tankowania
            - Dodanie wymiany opon
            - Dodanie wymiany oleju
            - Dodanie przeglądu technicznego
            - Dodanie stłuczki
- Podklasy dziedziczące po klasie Pojazd:
    - Tankowanie
    - SerwisOpon
    - SerwisOleju
    - PrzeglądTechniczny
    - Wypadek
        - Metody (+po 2 poniższe metody dla każdej z podklas):
            - Wypisanie wszystkich operacji w klasie np. Tankowanie
            - Wypisanie operacji dla danego pojazdu
"""

from datetime import date
from pojazd import Pojazd, Tankowanie, SerwisOpon, SerwisOleju, PrzegladTechniczny, Wypadek


def main():
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

    poj = Pojazd()
    tan = Tankowanie(date.today())
    sop = SerwisOpon(date.today())
    sol = SerwisOleju(date.today())
    prz = PrzegladTechniczny(date.today(), date.today())
    wyp = Wypadek(date.today(), 0, 0)

    pojazdy = (
        (None, 'Audi', 'A4', 2015, "GD999LR", 120000),
        (None, 'Peugeot', '406', 2019, "WA123CS", 145000),
        (None, 'Peugeot', '406', 2020, "ST245DF", 155000),
        (None, 'Nissan', 'Pathfinder', 2013, "GT987PK", 178000),
        (None, 'Nissan', 'Patrol', 2005, "GS942LY", 198000),
        (None, 'Ford', 'Transit', 2023, "GA223RR", 80000),
        (None, 'Opel', 'Movano', 2006, "RT259LL", 47550),
        (None, 'Ford', 'Transit', 2003, "PO463AS", 408000)
    )

    # poj.dodaj_pojazdy(pojazdy)

    def menu():
        print('-' * 40)
        print('--- MENU GŁÓWNE --- Wybierz z menu 0-9: ')
        print('-' * 40)
        print('1 - Wypisz wszystkie pojazdy')
        print('2 - Dodaj pojazd')
        print('3 - Usuń pojazd')
        print('4 - Zmień przebieg pojazdu')
        print('5 -> Tankowanie')
        print('6 -> Przegląd techniczny')
        print('7 -> Serwis opon')
        print('8 -> Serwis oleju')
        print('9 -> Wypadek')
        print('0 - >> Wyjdź <<')
        print('-' * 30)

    def menu_tankowania():
        print('- Stacja paliw -')
        print('1 - Zatankuj')
        print('2 - Wypisz wszystkie tankowania')
        print('3 - Wypisz tankowania dla pojazdu')
        print('0 - Wróć do głównego menu')
        print('-' * 15)

    def menu_przeglady():
        print('- Stacja kontroli -')
        print('1 - Dodaj przegląd')
        print('2 - Wypisz wszystkie przeglądy')
        print('3 - Wypisz przeglądy dla pojazdu')
        print('0 - Wróć do głównego menu')
        print('-' * 15)

    def menu_oleju():
        print('- Warsztat oleju -')
        print('1 - Dodaj serwis oleju')
        print('2 - Wypisz wszystkie serwisy oleju')
        print('3 - Wypisz serwisy oleju dla pojazdu')
        print('0 - Wróć do głównego menu')
        print('-' * 15)

    def menu_opon():
        print('- Warsztat opon -')
        print('1 - Dodaj serwis opon')
        print('2 - Wypisz wszystkie serwisy opon')
        print('3 - Wypisz serwisy opon dla pojazdu')
        print('0 - Wróć do głównego menu')
        print('-' * 15)

    def menu_wypadki():
        print('- Kolizje i stłuczki -')
        print('1 - Dodaj wypadek')
        print('2 - Wypisz wszystkie wypadki')
        print('3 - Wypisz wypadki dla pojazdu')
        print('0 - Wróć do głównego menu')
        print('-' * 15)

    while True:
        pojazdy = (
            (None, 'Audi', 'A4', 2015, "GD999LR", 120000),
            (None, 'Peugeot', '406', 2019, "WA123CS", 145000),
            (None, 'Peugeot', '406', 2020, "ST245DF", 155000),
            (None, 'Nissan', 'Pathfinder', 2013, "GT987PK", 178000),
            (None, 'Nissan', 'Patrol', 2005, "GS942LY", 198000),
            (None, 'Ford', 'Transit', 2023, "GA223RR", 80000),
            (None, 'Opel', 'Movano', 2006, "RT259LL", 47550),
            (None, 'Ford', 'Transit', 2003, "PO463AS", 408000)
        )

        # poj.dodaj_pojazdy(pojazdy)
        try:
            menu()
            choice = int(input('Co chcesz zrobić? Podaj numer z menu: '))
            print('-' * 30)
            if choice == 1:
                poj.wypisz_pojazdy()
                continue
            elif choice == 2:
                poj.dodaj_pojazd()
                continue
            elif choice == 3:
                poj.usun_pojazd()
                continue
            elif choice == 4:
                poj.zmien_przebieg_pojazdu()
                continue
            elif choice == 5:
                menu_tankowania()
                t_menu = int(input('Tankowanie - podaj numer z menu: '))
                if t_menu == 1:
                    tan.dodaj_tankowanie_pojazdu()
                elif t_menu == 2:
                    tan.wypisz_wszystkie_tankowania()
                elif t_menu == 3:
                    tan.wypisz_tankowania_pojazdu()
                elif t_menu == 0:
                    menu()
                continue
            elif choice == 6:
                menu_przeglady()
                p_menu = int(input('Przeglądy - podaj numer z menu: '))
                if p_menu == 1:
                    prz.dodaj_przeglad_techniczny()
                elif p_menu == 2:
                    prz.wypisz_wszystkie_przeglady()
                elif p_menu == 3:
                    prz.wypisz_przeglady_pojazdu()
                elif p_menu == 0:
                    menu()
                continue
            elif choice == 7:
                menu_opon()
                op_menu = int(input('Opony - podaj numer z menu: '))
                if op_menu == 1:
                    sop.dodaj_serwis_opon()
                elif op_menu == 2:
                    sop.wypisz_wszystkie_wymiany_opon()
                elif op_menu == 3:
                    sop.wypisz_wymiany_opon_pojazdu()
                elif op_menu == 0:
                    menu()
                continue
            elif choice == 8:
                menu_oleju()
                ol_menu = int(input('Olej - podaj numer z menu: '))
                if ol_menu == 1:
                    sol.dodaj_serwis_oleju()
                elif ol_menu == 2:
                    sol.wypisz_wszystkie_wymiany_oleju()
                elif ol_menu == 3:
                    sol.wypisz_wymiany_oleju_pojazdu()
                elif ol_menu == 0:
                    menu()
                continue
            elif choice == 9:
                menu_wypadki()
                w_menu = int(input('Wypadki - podaj numer z menu: '))
                if w_menu == 1:
                    wyp.dodaj_wypadek_pojazdu()
                elif w_menu == 2:
                    wyp.wypisz_wszystkie_wypadki()
                elif w_menu == 3:
                    wyp.wypisz_wypadki_pojazdu()
                elif w_menu == 0:
                    menu()
                continue
            elif choice == 0:
                print('Do zobaczenia!')
                break
            else:
                print('Zły wybór, spróbuj ponownie: ')
                menu()

        except ValueError:
            print('~~~~~')
            print('Błąd, wybrano literę lub inny znak. Wybierz 0-9: ')
            print('~~~~~')
            continue

        if choice not in range(0, 9):
            print('~~~~~')
            print('Zły wybór, numer poza zasięgiem menu. Wybierz 0-9: ')
            print('~~~~~')
            continue

        return choice



if __name__ == '__main__':
    main()

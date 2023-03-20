import datetime
import sqlite3
import sqlite3 as sql
from sqlite3 import Error
from datetime import date
from prettytable import PrettyTable, MSWORD_FRIENDLY
from datetime import timedelta

# Tworzenie bazy, połączenia i kursora
conn = sql.connect('flota.db')
conn.row_factory = sql.Row
cursor = conn.cursor()
try:
    # tworzenie tabeli pojazdów
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pojazdy (
            id integer PRIMARY KEY,
            marka text NOT NULL,
            model text NOT NULL,
            rocznik text NOT NULL,
            rejestracja text NOT NULL,
            przebieg integer NOT NULL,
                UNIQUE (rejestracja)
        )""")
except Error as e:
    print(e)
try:
    # tworzenie tabeli tankowań
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tankowania (
            id integer PRIMARY KEY,
            data_tankowania date NOT NULL,
            zatankowano float NOT NULL,
            stary_licznik integer NOT NULL,
            nowy_licznik integer NOT NULL,
            pojazd_id integer NOT NULL,
            FOREIGN KEY (pojazd_id) REFERENCES pojazdy (id)
        )""")
except Error as e:
    print(e)
try:
    # tworzenie tabeli serwisu opon
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS serwis_opon (
            id integer PRIMARY KEY,
            data_serwisu_opon date NOT NULL,
            przebieg integer NOT NULL,
            pojazd_id integer NOT NULL,
            FOREIGN KEY (pojazd_id) REFERENCES pojazdy (id)
        )""")
except Error as e:
    print(e)
try:
    # tworzenie tabeli serwisu oleju
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS serwis_oleju (
            id integer PRIMARY KEY,
            data_serwisu_oleju date NOT NULL,
            przebieg integer NOT NULL,
            pojazd_id integer NOT NULL,
            FOREIGN KEY (pojazd_id) REFERENCES pojazdy (id)
        )""")
except Error as e:
    print(e)
try:
    # tworzenie tabeli przeglądów technicznych
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS przeglady (
            id integer PRIMARY KEY,
            data_przegladu date NOT NULL,
            przebieg integer NOT NULL,
            data_waznosci date NOT NULL,
            pojazd_id integer NOT NULL,
            FOREIGN KEY (pojazd_id) REFERENCES pojazdy (id)
        )""")
except Error as e:
    print(e)
try:
    # tworzenie tabeli wypadków
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wypadki (
            id integer PRIMARY KEY,
            data_wypadku date NOT NULL,
            ofiary_smiertelne int,
            ranni int,
            pojazd_id integer NOT NULL,
            FOREIGN KEY (pojazd_id) REFERENCES pojazdy (id)
        )""")
except Error as e:
    print(e)

conn.commit()

# Funkcja zwracająca nazwę funkcji, w której wystąpił błąd.
def check_function(func):
    def wrapper_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (sql.OperationalError, sql.IntegrityError):
            print(f'Funkcja {func.__name__} zwróciła błąd.')
            return None
    return wrapper_function

# Dekorator funkcji sprawdzającej, czy zaistniał jakiś błąd?
# Dodajemy @check_function nad każdą metodą, którą chcemy sprawdzać.

# Deklaracja klasy głównej Pojazd
class Pojazd:
    # Ustawienie globalnej zmiennej typ, będzie dostępna w każdej podklasie, która dziedziczy po Pojeździe
    typ: str = 'Samochód'

    # Inicjalizacja głównych zmiennych pojazdu
    def __init__(self):
        self.id = None
        self.marka = None
        self.model = None
        self.rocznik = None
        self.rejestracja = None
        self.przebieg = None

    # Metoda do wypisywania listy wszystkich pojazdów
    def wypisz_pojazdy(self):
        print('Aktualna flota:')
        cursor.execute('SELECT pojazdy.id,marka,model,rocznik,rejestracja,przebieg '
                       'FROM pojazdy ORDER BY marka, rocznik')
        pojazdy = cursor.fetchall()
        table = PrettyTable(['ID', 'MARKA', 'MODEL', 'ROCZNIK', 'REJESTRACJA', 'PRZEBIEG'])
        table.set_style(MSWORD_FRIENDLY)
        for s in pojazdy:
            table.add_row(s)
        # Wypisujemy tabelę tylko jeżeli baza nie jest pusta, inaczej wypisujemy komunikat o błędzie.
        if len(pojazdy) != 0:
            print('-' * 64)
            print(table)
            print('-' * 64)
        else:
            print('Baza pojazdów jest pusta.')

    # Metoda do wypisania danych jednego pojazdu
    def wypisz_dane_pojazdu(self, _id):
        return f'{self.marka} {self.model} {self.rejestracja}'

    # Metoda usuwania pojazdu z wewnętrzną metodą wypisania danych danego pojazdu
    def usun_pojazd(self):
        print('\n~ Usuwanie pojazdu ~')
        _id = input('Który pojazd chcesz usunąć? Podaj id: ')
        wybrany = cursor.execute('SELECT pojazdy.id,marka,model,rejestracja FROM pojazdy WHERE id=?',
                                 (_id,)).fetchall()

        # Wewnętrzna metoda przekazująca dane pojazdu do linii 143, trzeba złapać id i dane,
        # zanim zostaną skasowane.
        def do_skasowania(_id):
            for row in wybrany:
                return f'id:{row[0]} {row[1]} {row[2]} {row[3]}'

        cursor.execute('DELETE FROM pojazdy WHERE id=?', (_id,))
        conn.commit()
        if cursor.rowcount:
            print('\nPojazd pomyślnie usunięto z bazy.', do_skasowania(_id))
            print('-' * 64)
        else:
            print('\nNie ma takiego id w bazie.')

    # Metoda dodawania pojazdu do bazy
    def dodaj_pojazd(self):
        try:
            print('\n~ Dodawanie pojazdu ~')
            self.marka = input('Podaj markę pojazdu: ')
            self.model = input('Podaj model: ')
            self.rocznik = int(input('Rok produkcji: '))
            self.rejestracja = input('Numer rejestracyjny (bez spacji): ')
            self.przebieg = int(input('Stan licznika: '))
            cursor.execute('INSERT INTO pojazdy VALUES(?,?,?,?,?,?)',
                           (None, self.marka, self.model, self.rocznik, self.rejestracja, self.przebieg))
            nowe_id = cursor.lastrowid
            # "cursor.lastrowid" daje dostęp do obiektu Pojazd i tym samym do danych poprzez
            # funkcję 'wypisz_dane_pojazdu()'
            dodano = self.wypisz_dane_pojazdu(nowe_id)
            conn.commit()
            print('-' * 64)
            print('\nDodano pojazd:', dodano)  # Tutaj nie trzeba funkcji wewnętrznej
            print('-' * 64)
        # wyłapujemy błąd integralności bazy na polu 'rejestracja' ustawionego na UNIQUE
        except sqlite3.IntegrityError:
            print('Błąd: Ten pojazd jest już w bazie.')

    # To jest metoda do pierwszego wypełnienia bazy 8 zdefiniowanymi pojazdami
    def dodaj_pojazdy(self, pojazdy):
        try:
            cursor.executemany('INSERT INTO pojazdy VALUES(?,?,?,?,?,?)', pojazdy)
            conn.commit()
        except:
            return
        # Odmiana słowa pojazd w zależności od ilości dodanych pojazdów.
        # 1 = pojazd, 2, 3, 4 = pojazdy, 5 i więcej = pojazdów
        if conn.total_changes == 1:
            odmiana = 'pojazd.'
        elif 2 <= conn.total_changes < 5:
            odmiana = 'pojadzy.'
        else:
            odmiana = 'pojazdów.'
        print('-' * 64)
        print(f'Dodano {conn.total_changes} {odmiana}')
        print('-' * 64)

    # Metoda do ręcznej zmiany przebiegu danego pojazdu
    def zmien_przebieg_pojazdu(self):
        print('\n~ Ręczna zmiana stanu licznika pojazdu ~')
        _id = int(input('Podaj id pojazdu: '))
        _przebieg = int(input('Podaj nowy stan licznika: '))
        cursor.execute('UPDATE pojazdy set przebieg=? WHERE id=?', (_przebieg, _id,))
        conn.commit()
        print('-' * 64)
        print('\nZaktualizowano pojazd:', self.wypisz_dane_pojazdu(_id), 'nowy przebieg:', _przebieg)
        print('-' * 64)

    # Metoda tankowania pojazdu z wewnętrznymi metodami wypisania danych danego pojazdu
    # oraz wyłapania poprzedniego stanu licznika
    def dodaj_tankowanie_pojazdu(self):
        print('\n~ Zgłoszenie tankowania pojazdu ~')
        self.data_tankowania = date.today().strftime("%d/%B/%Y")
        self.pojazd_id = int(input('Podaj id pojazdu: '))
        self.zatankowano = float(input('Ile litrów zatankowano (0.0): '))

        def stary_licznik():
            cursor.execute('SELECT przebieg FROM pojazdy WHERE id=? ORDER BY id DESC LIMIT 1',
                           (self.pojazd_id,))
            for row in cursor:
                return f'{row[0]}'

        def dane_pojazdu():
            wybrany = cursor.execute('SELECT pojazdy.id,marka,model,rejestracja FROM pojazdy WHERE id=?',
                                     (self.pojazd_id,))
            for row in wybrany:
                return f'id:{row[0]} {row[1]} {row[2]} {row[3]}'

        self.stary_licznik = stary_licznik()
        self.nowy_licznik = int(input('Podaj aktualny stan licznika: '))
        cursor.execute('INSERT INTO tankowania VALUES(?,?,?,?,?,?)',
                       (None, self.data_tankowania, self.zatankowano, self.stary_licznik, self.nowy_licznik,
                        self.pojazd_id))
        cursor.execute('UPDATE pojazdy set przebieg=? WHERE id=?', (self.nowy_licznik, self.pojazd_id,))
        conn.commit()
        print('-' * 64)
        print('\nZatankowano pojazd:', dane_pojazdu())
        print('-' * 64)

    # Metoda dodawania wymiany opon pojazdu z wewnętrzną metodą wypisania danych danego pojazdu
    def dodaj_serwis_opon(self):
        print('\n~ Zgłoszenie wymiany opon pojazdu ~')
        self.data_serwisu_opon = date.today().strftime("%d/%B/%Y")
        self.pojazd_id = int(input('Podaj id pojazdu: '))
        self.przebieg = int(input('Podaj aktualny stan licznika: '))

        def dane_pojazdu():
            wybrany = cursor.execute('SELECT pojazdy.id,marka,model,rejestracja FROM pojazdy WHERE id=?',
                                     (self.pojazd_id,))
            for row in wybrany:
                return f'id:{row[0]} {row[1]} {row[2]} {row[3]}'

        cursor.execute('INSERT INTO serwis_opon VALUES(?,?,?,?)',
                       (None, self.data_serwisu_opon, self.przebieg, self.pojazd_id))
        conn.commit()
        print('-' * 64)
        print('\nWymieniono opony pojazdu:', dane_pojazdu())
        print('-' * 64)

    # Metoda dodawania wymiany oleju pojazdu z wewnętrzną metodą wypisania danych danego pojazdu
    def dodaj_serwis_oleju(self):
        print('\n~ Zgłoszenie wymiany oleju pojazdu ~')
        self.data_serwisu_oleju = date.today().strftime("%d/%B/%Y")
        self.pojazd_id = int(input('Podaj id pojazdu: '))
        self.przebieg = int(input('Podaj aktualny stan licznika: '))

        def dane_pojazdu():
            wybrany = cursor.execute('SELECT pojazdy.id,marka,model,rejestracja FROM pojazdy WHERE id=?',
                                     (self.pojazd_id,))
            for row in wybrany:
                return f'id:{row[0]} {row[1]} {row[2]} {row[3]}'

        cursor.execute('INSERT INTO serwis_oleju VALUES(?,?,?,?)',
                       (None, self.data_serwisu_oleju, self.przebieg, self.pojazd_id))
        conn.commit()
        print('-' * 64)
        print('\nWymieniono olej pojazdu:', dane_pojazdu())
        print('-' * 64)

    # Metoda dodawania przeglądu technicznego pojazdu z wewnętrzną metodą wypisania danych danego pojazdu
    def dodaj_przeglad_techniczny(self):
        print('\n~ Zgłoszenie przeglądu technicznego pojazdu ~')
        dzis = datetime.datetime.today().strftime("%d/%B/%Y")
        self.data_serwisu_oleju = dzis
        self.pojazd_id = int(input('Podaj id pojazdu: '))
        self.przebieg = int(input('Podaj aktualny stan licznika: '))
        out = datetime.datetime.strptime(dzis, "%d/%B/%Y") + timedelta(days=365)
        self.data_waznosci = out.strftime("%d/%B/%Y")

        def dane_pojazdu():
            wybrany = cursor.execute('SELECT pojazdy.id,marka,model,rejestracja FROM pojazdy WHERE id=?',
                                     (self.pojazd_id,))
            for row in wybrany:
                return f'id:{row[0]} {row[1]} {row[2]} {row[3]}'

        cursor.execute('INSERT INTO przeglady VALUES(?,?,?,?,?)',
                       (None, self.data_serwisu_oleju, self.przebieg, self.data_waznosci, self.pojazd_id))
        conn.commit()
        print('-' * 64)
        print('\nPrzegląd techniczny pojazdu:', dane_pojazdu())
        print('-' * 64)

    # Metoda dodawania wypadku pojazdu z wewnętrzną metodą wypisania danych danego pojazdu
    def dodaj_wypadek_pojazdu(self):
        print('\n~ Zgłoszenie wypadku pojazdu ~')
        self.data_wypadku = date.today().strftime("%d/%B/%Y")
        self.pojazd_id = int(input('Podaj id pojazdu: '))
        self.ofiary_smiertelne = int(input('Podaj ilość ofiar: '))
        self.ranni = int(input('Podaj ilość rannych: '))

        def dane_pojazdu():
            wybrany = cursor.execute('SELECT pojazdy.id,marka,model,rejestracja FROM pojazdy WHERE id=?',
                                     (self.pojazd_id,))
            for row in wybrany:
                return f'id:{row[0]} {row[1]} {row[2]} {row[3]}'

        cursor.execute('INSERT INTO wypadki VALUES(?,?,?,?,?)',
                       (None, self.data_wypadku, self.ofiary_smiertelne, self.ranni, self.pojazd_id))
        conn.commit()
        print('-' * 64)
        print('\nWypadki pojazdu:', dane_pojazdu())
        print('-' * 64)


# Deklaracja klasy dziedziczącej po klasie Pojazd
class Tankowanie(Pojazd):
    # Inicjalizacja zmiennej lokalnej data_tankowania oraz zmiennych z klasy 'parent'
    def __init__(self, data_tankowania: date, _id=None, _marka=None, _model=None, _rocznik=None, _rejestracja=None,
                 _przebieg=None):
        # Inicjalizacja klasy nadrzędnej Pojazd
        super().__init__()
        self.data_tankowania = data_tankowania

    # Metoda wypisania listy tankowań
    def wypisz_wszystkie_tankowania(self):
        print('\n~ Rejestr tankowań ~')
        cursor.execute('SELECT tankowania.id,data_tankowania,zatankowano,nowy_licznik,'
                       'pojazdy.marka,model,rejestracja '
                       'FROM tankowania '
                       'INNER JOIN pojazdy ON tankowania.pojazd_id = pojazdy.id')
        pojazdy = cursor.fetchall()
        table = PrettyTable(['ID', 'DATA', 'LITRÓW', 'NOWY LICZNIK', 'MARKA', 'MODEL', 'REJESTRACJA'])
        table.set_style(MSWORD_FRIENDLY)
        for s in pojazdy:
            table.add_row(s)
        if len(pojazdy) != 0:
            print('\nLista wszystkich tankowań:')
            print('-' * 78)
            print(table)
            print('-' * 78)
        else:
            print('Brak tankowań.')

    # Metoda wypisania listy tankowań dla danego pojazdu z metodą wewnętrzną wyłapującą dane pojazdu do nagłówka
    def wypisz_tankowania_pojazdu(self):
        print('\n~ Rejestr tankowań pojazdu ~')
        _id = int(input('Podaj id pojazdu: '))

        def naglowek():
            cursor.execute('SELECT pojazdy.marka,pojazdy.model,pojazdy.rejestracja '
                           'FROM pojazdy '
                           'INNER JOIN tankowania ON pojazdy.id = tankowania.pojazd_id '
                           'WHERE pojazd_id=?', (_id,))
            for row in cursor:
                return f'Typ: {self.typ}, {row[0]} {row[1]} {row[2]}'

        cursor.execute('SELECT tankowania.data_tankowania,tankowania.zatankowano,'
                       'tankowania.nowy_licznik AS tp,tankowania.stary_licznik AS pp,'
                       '(tankowania.nowy_licznik - tankowania.stary_licznik) || " km" AS dystans,'
                       'ROUND((tankowania.zatankowano / (tankowania.nowy_licznik - tankowania.stary_licznik) * 100),2) '
                       '|| " l/100" AS spalanie '
                       'FROM tankowania '
                       'INNER JOIN pojazdy ON tankowania.pojazd_id = pojazdy.id '
                       'WHERE pojazd_id=?', (_id,))

        pojazdy = cursor.fetchall()
        table = PrettyTable(['DATA', 'LITRÓW', 'NOWY LICZNIK', 'STARY LICZNIK',
                             'PRZEJECHANO', 'ŚR. SPALANIE'])
        table.set_style(MSWORD_FRIENDLY)
        for s in pojazdy:
            table.add_row(s)
        if len(pojazdy) != 0:
            print('\nLista tankowań dla pojazdu:', naglowek())
            print('-' * 86)
            print(table)
            print('-' * 86)
        else:
            print('Brak tankowań.')


# Ten sam schemat co w klasie Tankowanie
class SerwisOpon(Pojazd):
    def __init__(self, data_opon: date, _id=None, _marka=None, _model=None, _rocznik=None, _rejestracja=None,
                 _przebieg=None):
        super().__init__()
        self.data_serwisu_opon = data_opon

    # Metoda wypisania listy serwisów opon
    def wypisz_wszystkie_wymiany_opon(self):
        print('\n~ Rejestr serwisów opon ~')
        cursor.execute('SELECT serwis_opon.id,data_serwisu_opon,serwis_opon.przebieg AS sop,'
                       'pojazdy.marka,model,rejestracja '
                       'FROM serwis_opon '
                       'INNER JOIN pojazdy ON serwis_opon.pojazd_id = pojazdy.id')
        pojazdy = cursor.fetchall()
        table = PrettyTable(['ID', 'DATA', 'PRZEBIEG', 'MARKA', 'MODEL', 'REJESTRACJA'])
        table.set_style(MSWORD_FRIENDLY)
        for s in pojazdy:
            table.add_row(s)
        if len(pojazdy) != 0:
            print('\nLista wszystkich wymian opon:')
            print('-' * 66)
            print(table)
            print('-' * 66)
        print('Brak wymian opon.')

    # Metoda wypisania listy serwisów opon dla danego pojazdu z metodą wewnętrzną wyłapującą dane pojazdu
    # do nagłówka
    def wypisz_wymiany_opon_pojazdu(self):
        print('\n~ Rejestr serwisów opon pojazdu ~')
        _id = int(input('Podaj id pojazdu: '))

        def naglowek():
            cursor.execute('SELECT pojazdy.marka,pojazdy.model,pojazdy.rejestracja '
                           'FROM pojazdy '
                           'INNER JOIN serwis_opon ON pojazdy.id = serwis_opon.pojazd_id '
                           'WHERE pojazd_id=?', (_id,))
            for row in cursor:
                return f'Typ: {self.typ}, {row[0]} {row[1]} {row[2]}'

        cursor.execute('SELECT serwis_opon.data_serwisu_opon,serwis_opon.przebieg AS sop '
                       'FROM serwis_opon '
                       'INNER JOIN pojazdy ON serwis_opon.pojazd_id = pojazdy.id '
                       'WHERE pojazd_id=?', (_id,))

        pojazdy = cursor.fetchall()
        table = PrettyTable(['DATA', 'PRZEBIEG'])
        table.set_style(MSWORD_FRIENDLY)
        for s in pojazdy:
            table.add_row(s)
        if len(pojazdy) != 0:
            print('\nLista serwisów opon dla pojazdu:', naglowek())
            print('-' * 64)
            print(table)
            print('-' * 64)
        else:
            print('Brak wymian opon.')


# Ten sam schemat co w klasach Tankowanie i SerwisOpon
class SerwisOleju(Pojazd):
    def __init__(self, data_oleju: date, _id=None, _marka=None, _model=None, _rocznik=None, _rejestracja=None,
                 _przebieg=None):
        super().__init__()
        self.data_serwisu_oleju = data_oleju

    # Metoda wypisująca listę serwisów oleju
    def wypisz_wszystkie_wymiany_oleju(self):
        print('\n~ Rejestr serwisów oleju ~')
        cursor.execute('SELECT serwis_oleju.id,data_serwisu_oleju,serwis_oleju.przebieg AS solp,'
                       'pojazdy.marka,model,rejestracja '
                       'FROM serwis_oleju '
                       'INNER JOIN pojazdy ON serwis_oleju.pojazd_id = pojazdy.id')
        pojazdy = cursor.fetchall()
        table = PrettyTable(['ID', 'DATA', 'PRZEBIEG', 'MARKA', 'MODEL', 'REJESTRACJA'])
        table.set_style(MSWORD_FRIENDLY)
        for s in pojazdy:
            table.add_row(s)
        if len(pojazdy) != 0:
            print('\nLista wszystkich wymian oleju:')
            print('-' * 70)
            print(table)
            print('-' * 70)
        else:
            print('Brak wymian oleju.')

    # Metoda wypisania listy serwisów oleju dla danego pojazdu z metodą wewnętrzną wyłapującą dane pojazdu
    # do nagłówka
    def wypisz_wymiany_oleju_pojazdu(self):
        print('\n~ Rejestr serwisów oleju pojazdu ~')
        _id = int(input('Podaj id pojazdu: '))

        def naglowek():
            cursor.execute('SELECT pojazdy.marka,pojazdy.model,pojazdy.rejestracja '
                           'FROM pojazdy '
                           'INNER JOIN serwis_oleju ON pojazdy.id = serwis_oleju.pojazd_id '
                           'WHERE pojazd_id=?', (_id,))
            for row in cursor:
                return f'Typ: {self.typ}, {row[0]} {row[1]} {row[2]}'

        cursor.execute('SELECT serwis_oleju.data_serwisu_oleju,serwis_oleju.przebieg AS sop '
                       'FROM serwis_oleju '
                       'INNER JOIN pojazdy ON serwis_oleju.pojazd_id = pojazdy.id '
                       'WHERE pojazd_id=?', (_id,))

        pojazdy = cursor.fetchall()
        table = PrettyTable(['DATA', 'PRZEBIEG'])
        table.set_style(MSWORD_FRIENDLY)
        for s in pojazdy:
            table.add_row(s)
        if len(pojazdy) != 0:
            print('\nLista serwisów oleju dla pojazdu:', naglowek())
            print('-' * 64)
            print(table)
            print('-' * 64)
        else:
            print('Brak wymian oleju.')


# Ten sam schemat co w klasach Tankowanie, SerwisOpon, SerwisOleju
class PrzegladTechniczny(Pojazd):
    def __init__(self, data_przegladu: date, data_waznosci: date, _id=None, _marka=None, _model=None,
                 _rocznik=None, _rejestracja=None, _przebieg=None):
        super().__init__()
        self.data_przegladu = data_przegladu
        self.data_waznosci = data_waznosci

    # Metdoa wypisująca listę przeglądów technicznych
    def wypisz_wszystkie_przeglady(self):
        print('\n~ Rejestr przeglądów ~')
        cursor.execute('SELECT przeglady.id,data_przegladu,przeglady.przebieg AS ppt,data_waznosci,'
                       'pojazdy.marka,model,rejestracja '
                       'FROM przeglady '
                       'INNER JOIN pojazdy ON przeglady.pojazd_id = pojazdy.id')
        pojazdy = cursor.fetchall()
        table = PrettyTable(['ID', 'DATA PRZEGLĄDU', 'PRZEBIEG', 'WAŻNY DO', 'MARKA', 'MODEL', 'REJESTRACJA'])
        table.set_style(MSWORD_FRIENDLY)
        for s in pojazdy:
            table.add_row(s)
        if len(pojazdy) != 0:
            print('\nLista wszystkich przeglądów technicznych:')
            print('-' * 83)
            print(table)
            print('-' * 83)
        else:
            print('Brak przeglądów.')

    # Metoda wypisania listy przeglądów dla danego pojazdu z metodą wewnętrzną wyłapującą dane pojazdu do nagłówka
    def wypisz_przeglady_pojazdu(self):
        print('\n~ Rejestr przeglądów pojazdu ~')
        _id = int(input('Podaj id pojazdu: '))

        def naglowek():
            cursor.execute('SELECT pojazdy.marka,pojazdy.model,pojazdy.rejestracja '
                           'FROM pojazdy '
                           'INNER JOIN przeglady ON pojazdy.id = przeglady.pojazd_id '
                           'WHERE pojazd_id=?', (_id,))
            for row in cursor:
                return f'Typ: {self.typ}, {row[0]} {row[1]} {row[2]}'

        cursor.execute('SELECT przeglady.data_przegladu,przeglady.przebieg AS ppt,przeglady.data_waznosci '
                       'FROM przeglady '
                       'INNER JOIN pojazdy ON przeglady.pojazd_id = pojazdy.id '
                       'WHERE pojazd_id=?', (_id,))

        pojazdy = cursor.fetchall()
        table = PrettyTable(['DATA', 'PRZEBIEG', 'WAŻNY DO'])
        table.set_style(MSWORD_FRIENDLY)
        for s in pojazdy:
            table.add_row(s)
        if len(pojazdy) != 0:
            print('\nLista przeglądów dla pojazdu:', naglowek())
            print('-' * 64)
            print(table)
            print('-' * 64)
        else:
            print('Brak przeglądów.')


# Ten sam schemat co w klasach Tankowanie, SerwisOpon, SerwisOleju oraz PrzegladTechniczny
class Wypadek(Pojazd):
    def __init__(self, data_wypadku: date, ofiary_smiertelne: int, ranni: int, _id=None, _marka=None, _model=None,
                 _rocznik=None, _rejestracja=None, _przebieg=None):
        super().__init__()
        self.data_wypadku = data_wypadku
        self.ofiary_smiertelne = ofiary_smiertelne
        self.ranni = ranni

    # Metoda wypisania listy wypadków floty
    def wypisz_wszystkie_wypadki(self):
        print('\n~ Rejestr wypadków ~')
        cursor.execute('SELECT wypadki.id,data_wypadku,ofiary_smiertelne,ranni,'
                       'pojazdy.marka,model,rejestracja '
                       'FROM wypadki '
                       'INNER JOIN pojazdy ON wypadki.pojazd_id = pojazdy.id')
        pojazdy = cursor.fetchall()
        table = PrettyTable(['ID', 'DATA', 'OFIARY', 'RANNI', 'MARKA', 'MODEL', 'REJESTRACJA'])
        table.set_style(MSWORD_FRIENDLY)
        for s in pojazdy:
            table.add_row(s)
        if len(pojazdy) != 0:
            print('\nLista wszystkich wypadków:')
            print('-' * 75)
            print(table)
            print('-' * 75)
        else:
            print('Brak wypadków.')

    # Metoda wypisania listy wypadków dla danego pojazdu z metodą wewnętrzną wyłapującą dane pojazdu do nagłówka
    def wypisz_wypadki_pojazdu(self):
        print('\n~ Rejestr wypadków pojazdu ~')
        _id = int(input('Podaj id pojazdu: '))

        def naglowek():
            cursor.execute('SELECT pojazdy.marka,pojazdy.model,pojazdy.rejestracja '
                           'FROM pojazdy '
                           'INNER JOIN wypadki ON pojazdy.id = wypadki.pojazd_id '
                           'WHERE pojazd_id=?', (_id,))

            for row in cursor:
                return f'Typ: {self.typ}, {row[0]} {row[1]} {row[2]}'

        cursor.execute('SELECT wypadki.data_wypadku,ofiary_smiertelne,ranni '
                       'FROM wypadki '
                       'INNER JOIN pojazdy ON wypadki.pojazd_id = pojazdy.id '
                       'WHERE pojazd_id=?', (_id,))

        pojazdy = cursor.fetchall()
        table = PrettyTable(['DATA', 'OFIARY', 'RANNI'])
        table.set_style(MSWORD_FRIENDLY)
        for s in pojazdy:
            table.add_row(s)
        if len(pojazdy) != 0:
            print('\nLista wypadków dla pojazdu:', naglowek())
            print('-' * 64)
            print(table)
            print('-' * 64)
        else:
            print('Brak wypadków.')

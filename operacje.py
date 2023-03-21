import datetime
from datetime import date


class Operacja:
    def __init__(self, data_operacji: date, przebieg: int):
        self.data_operacji = data_operacji
        self.przebieg = przebieg

    def wypisz_operacje(self):
        pass

    @staticmethod
    def stworz_operacje():
        pass


class PrzegladTechniczny(Operacja):
    def __init__(self, data_operacji: date, status: bool, przebieg: int):
        super().__init__(data_operacji, przebieg)
        self.status = status

    def wypisz_operacje(self):
        data_waznosci = self.data_operacji.replace(year=self.data_operacji.year + 1)
        print(f'Przegląd Techniczny - Data przeglądu: {self.data_operacji}, '
              f'Przebieg: {self.przebieg} '
              f'Data ważności: {data_waznosci}, '
              f'Status: {self.status}')

    @staticmethod
    def stworz_operacje():
        print('\n~ Zgłoszenie przeglądu technicznego pojazdu ~')
        data_operacji = datetime.datetime.today()
        przebieg = int(input('Podaj aktualny stan licznika: '))
        return PrzegladTechniczny(data_operacji, True, przebieg)


class SerwisOleju(Operacja):
    def __init__(self, data_operacji: date, przebieg: int):
        super().__init__(data_operacji, przebieg)

    def wypisz_operacje(self):
        print(f'Serwis Oleju - Data przeglądu: {self.data_operacji} '
              f'Przebieg: {self.przebieg}')

    @staticmethod
    def stworz_operacje():
        print('\n~ Zgłoszenie wymiany oleju pojazdu ~')
        data_operacji = datetime.datetime.today()
        przebieg = int(input('Podaj aktualny stan licznika: '))
        return SerwisOleju(data_operacji, przebieg)


class SerwisOpon(Operacja):
    def __init__(self, data_operacji: date, przebieg: int):
        super().__init__(data_operacji, przebieg)

    def wypisz_operacje(self):
        print(f'Serwis Opon - Data przeglądu: {self.data_operacji} '
              f'Przebieg: {self.przebieg}')

    @staticmethod
    def stworz_operacje():
        print('\n~ Zgłoszenie wymiany opon pojazdu ~')
        data_operacji = datetime.datetime.today()
        przebieg = int(input('Podaj aktualny stan licznika: '))
        return SerwisOpon(data_operacji, przebieg)


class Tankowanie(Operacja):
    def __init__(self, data_operacji: date, przebieg: int, zatankowano: float):
        super().__init__(data_operacji, przebieg)
        self.zatankowano = zatankowano

    def wypisz_operacje(self):
        print(f'Tankowanie - Data tankowania: {self.data_operacji} '
              f'Przebieg: {self.przebieg}')

    @staticmethod
    def stworz_operacje():
        print('\n~ Zgłoszenie tankowania pojazdu ~')
        data_operacji = datetime.datetime.today()
        przebieg = int(input('Podaj aktualny stan licznika: '))
        zatankowano = float(input('Ile litrów zatankowano (0.0): '))
        return Tankowanie(data_operacji, przebieg, zatankowano)


class Wypadek(Operacja):
    def __init__(self, data_operacji: date, przebieg: int, ofiary_smiertelne: int, ranni: int):
        super().__init__(data_operacji, przebieg)
        self.ofiary_smiertelne = ofiary_smiertelne
        self.ranni = ranni

    def wypisz_operacje(self):
        print(f'Wydadek - Data wypadku: {self.data_operacji} '
              f'Przebieg: {self.przebieg} '
              f'Ofiary Śmiertelne: {self.ofiary_smiertelne} '
              f'Ranni: {self.ranni}')

    @staticmethod
    def stworz_operacje():
        print('\n~ Zgłoszenie wypadku pojazdu ~')
        data_operacji = datetime.datetime.today()
        przebieg = int(input('Podaj aktualny stan licznika: '))
        ofiary_smiertelne = int(input('Podaj ilość ofiar: '))
        ranni = int(input('Podaj ilość rannych: '))
        return Wypadek(data_operacji, przebieg, ofiary_smiertelne, ranni)

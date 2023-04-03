import datetime
from datetime import date


class Operacja:
    def __init__(self, data_operacji: date):
        self.data_operacji = data_operacji

    def wypisz_operacje(self):
        pass

    @staticmethod
    def stworz_operacje():
        pass


class PrzegladTechniczny(Operacja):
    def __init__(self, data_operacji: date, status: bool):
        super().__init__(data_operacji)
        self.status = status

    def wypisz_operacje(self):
        data_waznosci = self.data_operacji.replace(year=self.data_operacji.year + 1)
        status = True if data_waznosci > datetime.date.today() else False
        self.status = status
        status_przegladu = 'Ważny' if status is True else 'Nieważny'
        dni_do_nastepnego_przegladu = data_waznosci - datetime.date.today()
        print(f'Data przeglądu: {self.data_operacji}, '
              f'Data ważności: {data_waznosci}, '
              f'Status: {status_przegladu} - dni do następnego przeglądu: {dni_do_nastepnego_przegladu.days}')

    @staticmethod
    def stworz_operacje():
        print('\n~ Zgłoszenie przeglądu technicznego pojazdu ~')
        data_operacji = datetime.datetime.today().date()
        return PrzegladTechniczny(data_operacji, True)


class SerwisOleju(Operacja):
    def __init__(self, data_operacji: date):
        super().__init__(data_operacji)

    def wypisz_operacje(self):
        print(f'Data wymiany oleju: {self.data_operacji}')

    @staticmethod
    def stworz_operacje():
        print('\n~ Zgłoszenie wymiany oleju pojazdu ~')
        data_operacji = datetime.datetime.today().date()
        return SerwisOleju(data_operacji)


class SerwisOpon(Operacja):
    def __init__(self, data_operacji: date):
        super().__init__(data_operacji)

    def wypisz_operacje(self):
        print(f'Data wymiany opon: {self.data_operacji}')

    @staticmethod
    def stworz_operacje():
        print('\n~ Zgłoszenie wymiany opon pojazdu ~')
        data_operacji = datetime.datetime.today().date()
        return SerwisOpon(data_operacji)


class Tankowanie(Operacja):
    def __init__(self, data_operacji: date, zatankowano: float):
        super().__init__(data_operacji)
        self.zatankowano = zatankowano
        self.spalanie = 0.0

    def zmien_spalanie(self, spalanie: float):
        self.spalanie = spalanie

    def wypisz_operacje(self):
        print(f'Data tankowania: {self.data_operacji} {"{:.2f}".format(self.spalanie)}')

    @staticmethod
    def stworz_operacje():
        print('\n~ Zgłoszenie tankowania pojazdu ~')
        data_operacji = datetime.datetime.today().date()
        zatankowano = float(input('Ile litrów zatankowano (0.0): '))
        return Tankowanie(data_operacji, zatankowano)


class Wypadek(Operacja):
    def __init__(self, data_operacji: date, ofiary_smiertelne: int, ranni: int):
        super().__init__(data_operacji)
        self.ofiary_smiertelne = ofiary_smiertelne
        self.ranni = ranni

    def wypisz_operacje(self):
        print(f'Data wypadku: {self.data_operacji} '
              f'Ofiary Śmiertelne: {self.ofiary_smiertelne} '
              f'Ranni: {self.ranni}')

    @staticmethod
    def stworz_operacje():
        print('\n~ Zgłoszenie wypadku pojazdu ~')
        data_operacji = datetime.datetime.today().date()
        ofiary_smiertelne = int(input('Podaj ilość ofiar: '))
        ranni = int(input('Podaj ilość rannych: '))
        return Wypadek(data_operacji, ofiary_smiertelne, ranni)

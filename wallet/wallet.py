"""This module contain basic Wallet class"""


class Wallet:
    """simple wallet class balance and currency"""
    def __init__(self, currency, balance):
        self.currency = self.is_valid_currency(currency)
        self.balance = self.is_valid_balance(balance)

    @staticmethod
    def is_valid_currency(currency):
        if not isinstance(currency, str):
            raise TypeError("Неверный тип валюты")
        elif len(currency) != 3:
            raise NameError('Неверная длина названия валюты')
        elif not currency.isupper(): # TODO
            raise ValueError('Название должно состоять только из заглавных букв')
        return currency

    @staticmethod
    def is_valid_balance(balance):
        if not isinstance(balance, (int, float)):
            raise TypeError('Баланс должен быть int или float')
        elif balance < 0:
            raise ValueError('Недоступен отрицательный баланс')
        return balance

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f'Wallet не поддерживает сравнение с {other}')
        elif self.currency != other.currency:
            raise ValueError('Нельзя сравнить разные валюты')
        return self.balance == other.balance

    def __add__(self, other):
        if not isinstance(other, Wallet):
            raise ValueError('Данная операция запрещена, разные типы данных')
        elif self.currency != other.currency:
            raise ValueError('Данная операция запрещена, доступно сложение одной валюты')
        return Wallet(self.currency, (self.balance + other.balance))

    def __sub__(self, other):
        if not isinstance(other, Wallet):
            raise ValueError('Данная операция запрещена, разные типы данных')
        elif self.currency != other.currency:
            raise ValueError('Данная операция запрещена, доступно вычитание одной валюты')
        elif other.balance > self.balance:
            raise ValueError('Запрещено вычитать больше чем есть, т.к. недоступен отрицательный баланс')
        return Wallet(self.currency, (self.balance - other.balance))




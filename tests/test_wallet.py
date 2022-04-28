'''This module contain basic unit tests for the wallet module
Their purpose to show how I use pytest framework '''
import pytest
from wallet.wallet import Wallet

#  test Wallet creation, marked with class_init_tests
@pytest.mark.class_init_tests
def test_currency_not_str():
    with pytest.raises(TypeError) as e:
        faulty_wallet = Wallet(1, 1)
        assert 'Неверный тип валюты' in str(e.value)

@pytest.mark.class_init_tests
def test_currency_len_not_3():
    with pytest.raises(NameError) as e:
        faulty_wallet = Wallet('RUBBB', 1)
        assert 'Неверная длина названия валюты' in str(e.value)

@pytest.mark.class_init_tests
def test_currency_is_not_upper():
    with pytest.raises(ValueError) as e:
        faulty_wallet = Wallet('rub', 1)
        assert 'Название должно состоять только из заглавных букв' in str(e.value)

@pytest.mark.class_init_tests
def test_balance_type_not_num():
    with pytest.raises(TypeError) as e:
        faulty_wallet = Wallet('RUB', 'rub')
        assert 'Баланс должен быть int или float' in str(e.value)

@pytest.mark.class_init_tests
def test_negative_balance_exception():
    with pytest.raises(ValueError) as e:
        faulty_wallet = Wallet('RUB', -1 )
        assert 'Недоступен отрицательный баланс' in str(e.value)


param_pairs = [
    ('RUB', 1), ('EUR', 1.99), ('USD', 0)]

@pytest.mark.class_init_tests
@pytest.mark.parametrize('currency, balance', param_pairs)
def test_wallet_creation(currency, balance):
    wallet = Wallet(currency, balance)
    assert wallet.currency == currency
    assert wallet.balance == balance

#  test class methods
@pytest.fixture
def correct_wallet():
    correct_wallet = Wallet('RUB', 10)
    return correct_wallet

#  test the equality
def test_not_eq_to_diff_class(correct_wallet):
    with pytest.raises(TypeError, match='Wallet не поддерживает сравнение с*') as e:
        correct_wallet == 2


def test_not_eq_different_currency(correct_wallet):
    with pytest.raises(ValueError, match='Нельзя сравнить разные валюты') as e:
        correct_wallet == Wallet('USD', 10)


def test_wallet_equals(correct_wallet):
    assert correct_wallet == Wallet('RUB', 10)
    assert correct_wallet == Wallet('RUB', 10.0)


def test_wallet_not_equal(correct_wallet):
    assert correct_wallet != Wallet('RUB', 9)


#  test the addition
def test_add_to_diff_class_exception(correct_wallet):
    with pytest.raises(ValueError, match='Данная операция запрещена, разные типы данных') as e:
        result = correct_wallet + 2


def test_add_diff_currency_exception(correct_wallet):
    with pytest.raises(ValueError, match='Данная операция запрещена, доступно сложение одной валюты') as e:
        wrong_cur_wallet = Wallet('EUR', 5)
        correct_wallet + wrong_cur_wallet


param_pairs = [
    ('RUB', 1), ('RUB', 1.0), ('RUB', 0)]

@pytest.mark.parametrize('currency, balance', param_pairs)
def test_add_to_wallet(correct_wallet, currency, balance):
    """Check result class type, sum"""
    other_wallet = Wallet(currency, balance)
    result_wallet = correct_wallet + other_wallet
    assert isinstance(result_wallet, Wallet), 'Result is not a Wallet class'
    assert result_wallet.balance == balance + 10, 'Wrong sum'

#  test subtraction
def test_sub_different_class_exception(correct_wallet):
    with pytest.raises(ValueError, match='Данная операция запрещена, разные типы данных') as e:
        result = correct_wallet - 2


def test_sub_different_currency_exception(correct_wallet):
    with pytest.raises(ValueError, match='Данная операция запрещена, доступно вычитание одной валюты') as e:
        wrong_cur_wallet = Wallet('EUR', 5)
        result = correct_wallet - wrong_cur_wallet


def test_sub_greater_value_exception(correct_wallet):
    with pytest.raises(ValueError, match='Запрещено вычитать больше чем есть, т.к. недоступен отрицательный баланс') as e:
        greater_balance_wallet = Wallet('RUB', 15)
        correct_wallet - greater_balance_wallet


param_pairs = [
    ('RUB', 1), ('RUB', 1.0), ('RUB', 0), ('RUB', 10)]

@pytest.mark.parametrize('currency, balance', param_pairs)
def test_positive_sub_from_wallet(correct_wallet, currency, balance):
    other_wallet = Wallet(currency, balance)
    result_wallet = correct_wallet - other_wallet
    assert isinstance(result_wallet, Wallet), 'Result is not a Wallet class'
    assert result_wallet.balance == 10 - balance, 'Wrong difference'

import pytest
from prostedodawanie import dodaj

def dodaj(a, b):
    return a + b

def test_dodaj_liczby_dodatnie():
    wynik = dodaj(2, 3)
    try:
        assert wynik == 5
        print("Test test_dodaj_liczby_dodatnie: Asercja spełniona")
    except AssertionError:
        print("Test test_dodaj_liczby_dodatnie: Asercja NIE została spełniona")
        raise

def test_dodaj_liczby_ujemne():
    wynik = dodaj(-1, -4)
    try:
        assert wynik == -5
        print("Test test_dodaj_liczby_ujemne: Asercja spełniona")
    except AssertionError:
        print("Test test_dodaj_liczby_ujemne: Asercja NIE została spełniona")
        raise

def test_dodaj_zero():
    wynik = dodaj(0, 5)
    try:
        assert wynik == 5
        print("Test test_dodaj_zero: Asercja spełniona")
    except AssertionError:
        print("Test test_dodaj_zero: Asercja NIE została spełniona")
        raise        
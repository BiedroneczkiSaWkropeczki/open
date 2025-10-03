#### Ćwiczenie nr 7:
# Zmodyfikuj program ponizej tak aby kwota, ilosc rat oraz oprocentowanie bylo 
# wprowadzane przez uzytkownika i uwzględnij, że w przypadku gdy użytkownik wprowadzi
# literę zamiast cyfry, przerwij program 

# Zdefiniowanie zmiennych
def get_user_input(parametr):
    data = ""
    while True:
        data = input(f"Podaj {parametr}: ")
        if not data.isnumeric():
            print("Prawdopodobnie podales literę")
        elif data.isnumeric():
            print("Dokonujemy konwersji")
            data = float(data)
            return data
        
def count_earnings():
    # Napisz funkcje ktora policzy oprocentowanie
    # Mozesz zaimplentowac takze funkcje main!
    pass

kwota = get_user_input('Kwota')
print(f'Podana kwota to {kwota}')

ilosc_lat = int(get_user_input('Ilosc Lat'))
print(f'Ilosc lat {ilosc_lat}')

oprocentowanie = get_user_input('Oprocentowanie')
print(f'Podane oprocentowanie {oprocentowanie}')



# print(f"Kwota wynosi {kwota}")

# kwota = float(input("Podaj kwotę: "))
# ilosc_lat = int(input("Podaj ilość lat: "))
# oprocentowanie = float(input("Podaj oprocentowanie: "))

# # Obliczenia
# kwota_koncowa = kwota * (1 + oprocentowanie / 100) ** ilosc_lat - kwota

# # Wynik
# print(f'Zysk wynosi {kwota_koncowa:.2f}')

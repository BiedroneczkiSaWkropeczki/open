kurs = 'Codebrainers'
typ_kursu = 'Tester'
grupa = kurs + typ_kursu
print(grupa)
# CodebrainersTester
# wyswietlanie apostrofow i cudzyslowiow
print("Test'Test'")
print('Test"Test"')
# wyswietlanie apostrofow i cudzyslowiow
print("Test'Test'")
print('Test"Test"')
print('Test\'Test')
print('Test"Test')
print("PierwszLinia\nDrugaLinia\nTrzeciaLinia\nCzwartaLinia\nPiataLinia")
# Znak specjalny \n
print('PierwszLinia\nDrugaLinia\nTrzeciaLinia\nCzwartaLinia\nPiataLinia')
print('PierwszaLinia' \
      'DrugaLinia' \
      'TrzeciaLinia' \
      'Czwarta' \
      'Piata')
print("""Test
      TEst
      Test""")
print('Informacje znajduja sie w katalogu C:\nowy katalog\testy')
print('Informacje znajduja sie w katalogu C:\nowy katalog\testy')
print(r'Informacje znajduja sie w katalogu C:\nowy katalog\testy')
print('©')

print('Informacje znajduja sie w katalogu C:\nowy katalog\testy')
print(r'Informacje znajduja sie w katalogu C:\nowy katalog\testy')
print('Copyright -> \u00A9')
print(r"Znaczek copyright jest ukryt pod tym kodem \u00A9")
print(r'<html><body><h1>Test</h1></body></html>')

print(word[0])  # P
print(word[1])  # y
print(word[2])  # t
print(word[3])  # h
print(word[4])  # o
print(word[5])  # n

word = 'Python'

print(word[0])
print(word[1])
print(word[10])

word = 'Python'
print(word[0])
print(word[1])
print(word[5])
print(word[-1])
print(word)
word = 'Python'
    #   012345
    #  -654321
# Pyt start - jest start, end - indeks ktory interesuje + 1 
print(word[0:3])        # Pyt
print(word[-2:-1])      # o
print(word[-3:])        # hon   - nie musimy wiedziec jak dlugi jest ciag znakow

kurs = 'Codebrainers'
nowy_kurs = kurs # kopia
nowy_kurs = kurs[:]
# co ile
print(kurs[0:-1:0.5])
# kurs[start:koniec:krok]

print(f'ilosc znakow {len(kurs)}')

kurs = 'Codebrainers'
nowy_kurs = kurs # kopia
nowy_kurs = kurs[:]
# co ile
print(kurs[0:-1:2])
# kurs[start:koniec:krok]
print(f'ilosc znakow {len(kurs)}')
print(kurs[0:len(kurs)])
t = [1, 2, 3]
print(t[2])
c = (1, 2, 3)
print(c[1])

#Patryk Walaszkowski 20:33
user_input = input('Tu wpisz swoje dane: ')
print(f'Wprowadziles {user_input}')
print(f'Wprowadzone dane sa typu {type(user_input)}')
# input() w wersji 3.x 
# raw_input() w wersji 2.x
user_input = input('Tu wpisz swoje dane: ')
print(f'Wprowadziles {user_input}')
print(f'Wprowadzone dane sa typu {type(user_input)}')
convert_str_to_int = int(user_input)
print(f'Po konwersji {type(convert_str_to_int)}')

#Patryk Walaszkowski 20:40
# input() w wersji 3.x 
# raw_input() w wersji 2.x
user_input = int(input('Tu wpisz swoje dane (liczbowe): '))
print(f'Wprowadziles {user_input}')
print(f'Wprowadzone dane sa typu {type(user_input)}')
# convert_str_to_int = int(user_input)
# print(f'Po konwersji {type(convert_str_to_int)}')

#Jan Gil 20:50

kwota = float(input("Podaj kwotę: "))
ilosc_lat = int(input("Podaj ilość lat: "))
oprocentowanie = float(input("Podaj oprocentowanie: "))
# Obliczenia
kwota_koncowa = kwota * (1 + oprocentowanie / 100) ** ilosc_lat - kwota
# Wynik
print(f'Zysk wynosi {kwota_koncowa:.2f}')


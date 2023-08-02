import pandas as pd
import numpy as np
# 1 Tworzenie series

count_km_swim = pd.Series(data=[3,4,5,4,5], index=("Pon", "Wt", "Środ", "Czw", "Pt"))

print (count_km_swim)
print('-----')

# 2 Tworzenie series 

meal_date = pd.Series(index=("Śniadanie", "Obiad", "Kolacja"), data=["jajecznica", "schabowy", "burger"], name="Posiłek")
print(meal_date)
print('-----')

# 3 Losowanie liczb z zakresu 20
ten = np.random.randn(20)
ten_Series = pd.Series(ten, name='losowanie liczb')

print(ten_Series)
print('-----')


# 4 słownik 
first_dict = {
    'Kawiarnia': 'Kawa',
    'Sklep': 'Zakupy',
    'Siłownia': 'Trening',
    'Wyjazd': 'Góry'
}

first_dict_series = pd.Series(first_dict, name='Co będę robił')

print(first_dict_series)
print('-----')


# 5 słownik series z nazwą 

price_dict = {
    'Kawa': 14,
    'Lody': 4,
    'Herbata': 5
}

price_dict_series = pd.Series(price_dict, name='Cena za produkty')
print(price_dict_series)
print('-----')

# 6 Wycinanie 
car = {
    'Audi': 'sedan',
    'Bmw': 'combi',
    'Mercedes': 'suv'
}

car_series = pd.Series(car)

car_series_bmw = car_series['Bmw']
print(car_series_bmw)
print('-----')

# 7 Czy dana wartość znajduje się
print ('Audi' in car_series)
print('-----')

# 8 Wycinanie liczb 
numner_tab = [10, 20, 30, 40, 50, 100]

numner_tab_series = pd.Series(numner_tab)
numner_tab_series_100 = numner_tab_series[0:3]
print(numner_tab_series_100)
print('-----')

# 9 Dodawanie wartości

tab1_add = [10, 50, 10]
tab2_add = [20, 50, 90]

tab1_add_series = pd.Series(tab1_add)
tab2_add_series = pd.Series(tab2_add)

all_tab1_tab2 = tab1_add_series.add(tab2_add_series)

print(all_tab1_tab2)
print('-----')

# 10  Odejmowanie wartości 

tab1_sub = [100, 100]
tab2_sub = [20, 30]

tab1_sub_series = pd.Series(tab1_sub)
tab2_sub_series = pd.Series(tab2_sub)

tab_all_series = tab1_sub_series.sub(tab2_sub_series)

print(tab_all_series)
print('-----')

# 11 Usuwanie duplikatów 
tab_duplicate = [100, 100, 100, 10, 20, 30, 100, 40]

tab_duplicate_series = pd.Series(tab_duplicate)

print(tab_duplicate_series.drop_duplicates())
print('-----')

# 12 Modyfikacja danej liczby 
modification_date = [200,300,400,600]

modification_date_series = pd.Series(modification_date)

modification_date_series[3] = 500

print (modification_date_series)
print('-----')

# Który indeks jest największy - max 
time_sport = {
    'pływanie': 1,
    'rower': 2,
    'bieg': 0.5
}

time_sport_series = pd.Series(time_sport)

print(time_sport_series.idxmax())
print('-----')

# Który indeks jest najmniejszy - min 

time_run = {
    'first_run': 2,
    'second_run': 4,
    'third_run': 1
}

time_run_series = pd.Series(time_run)

print(time_run_series.idxmin())
print('-----')

# count - ile rekordów 
name_girl = {
    'first': 'Ola',
    'second': 'Natalia',
    'third': 'Aga'
}

name_girl_series = pd.Series(name_girl)
print(name_girl_series.count())
print('-----')

# value_counts - ile mamy poszczególnych rekordów
coffee_drink = {
    'pon': 3,
    'wt:': 1,
    'śr': 1,
    'czw': 3,
    'piat': 1
}

coffee_drink_series = pd.Series(coffee_drink, name='Liczba rekordów')

print(coffee_drink_series.value_counts())
print('-----')

import pandas as pd


# top 2 poduktów 
price_drink = {
    "energy": 4,
    "coffee": 14,
    "tea": 5
}

price_drink_series = pd.Series(price_drink)

print(price_drink_series.nlargest(2))

# least 2 produkty
price_bike = {
    "argon": 10000,
    "canyon": 15000,
    "giant": 25000,
    "orbea": 17000
}

price_bike_series = pd.Series(price_bike)

print(price_bike_series.nsmallest(2))

# zaokrąglenie liczb do 2 miejsc 

time_record = {
    '100 m': 0.5467,
    '200 m' : 1.873,
    '400 m': 4.08712
}

time_record_series = pd.Series(time_record)

print(time_record_series.round(2))


# shift i fillna - przesuwanie wartości i zastąpienie czegoś 
list_of_product = {
    "wódka": 300,
    "piwo": 500, 
    "whisky": 100, 
    "drink": 50
}

list_of_product_series = pd.Series(list_of_product)

print(list_of_product_series.shift(2).fillna('Brak produktów'))

# sortowanie 
sort_product = {
    "jabłko": 3.99,
    "ananas": 5.99,
    "borówki": 9.99,
    "arbuz": 1.99
}

sort_product_sort = pd.Series(sort_product)

print(sort_product_sort.sort_values())

# sorotowanie od największych 

sort_name_place = {
    "zakopane": "z", 
    "Gdynia": "g",
    "Poznań": "p"
}

sort_name_place_series = pd.Series(sort_name_place)

print(sort_name_place_series.sort_values(key=lambda x: x.map({"z": 0, "p": 1, "g": 2})))

import pandas as pd

# Maksymalna wartości
number = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4
}

number_series = pd.Series(number)

print(number_series.aggregate(max))

print(number_series.nlargest(2))

# Minimalne wartości

number_big = {
    "100": 100, 
    "200": 200,
    "300": 300,
    "400": 400,
    "500": 500
}

number_big_series = pd.Series(number_big)

print(number_big_series.min())

print(number_big_series.nsmallest(3))

# Sumowanie wartości 

sum_number = {
    "200": 200,
    "400": 400
}

sum_number_series = pd.Series (sum_number)

print(str('Sumowana wartość: ') + str(sum_number_series.aggregate(sum)))

# Średnia wartość 

mean_number = [10, 30, 50]

mean_number_series = pd.Series(mean_number)

print(mean_number_series.mean())
print('----')

# suma, średnia, min, max 
test_number = [30, 30, 30, 10]

test_number_series = pd.Series(test_number)

print(test_number_series.aggregate(sum))
print(test_number_series.aggregate('mean'))
print(test_number_series.aggregate('max'))
print(test_number_series.aggregate('min'))

# apply - zamiana na wartości całkowite 
int_and_float = [10, 20.99, 11.22, 14.33, 16.21, 19.76]

int_and_float_series = pd.Series(int_and_float, name='Wartości całkowite')

print(int_and_float_series.apply(int))

# apply i lambda => zwiększenie liczby 10-krotnie 

number_lambda = [20, 40, 60]

number_lambda_series = pd.Series(number_lambda)

print(number_lambda_series.apply(lambda x: x * 10))

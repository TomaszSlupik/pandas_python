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
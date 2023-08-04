import pandas as pd 


modul = 'testowanie'
start = '2023-07-30'
end = '2023-07-31'

modul_two = 'implementacja'
start2 = '2023-08-05'
end2 = '2023-08-10'

test_one = [
    [modul, start, end, 'OK'],
    [modul_two, start2, end2, 'OK']
]

schema_test = [
        "MODUL",
        "START", 
        "KONIEC",
        "STATUS"
]


logi_all = pd.DataFrame(test_one, columns=schema_test)

print (logi_all)


# 2 DataFrame


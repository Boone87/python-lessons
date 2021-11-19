seasons = ['winter', 'spring', 'summer', 'autumn']
seasons_d = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}

month = int(input("Номер месяца "))

if month ==1 or month == 12 or month == 2:
    print(seasons_d.get(1))
    print(seasons[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_d.get(2))
    print(seasons[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons.get(3))
    print(seasons[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_d.get(4))
    print(seasons[3])
else:
    print("Не бывает месяца с такми значением")
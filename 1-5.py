dohod = int(input("Сколько вы заработали? "))
rashod = int(input("А сколько потратили? "))

if rashod < dohod:
    print(f"Фирма заработала {dohod - rashod}!")
    sotrydniki = int(input("сколько сотрудников у вас работает? "))
    zarplata = (dohod - rashod)/sotrydniki
    print(f"Каждый сотрудник заработал {int(zarplata)}")
elif rashod == dohod:
    print ("Вы вышли в ноль")
elif rashod > dohod:
    print ("Вы ушли в минус")
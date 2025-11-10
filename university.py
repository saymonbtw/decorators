from collections import defaultdict
from datetime import date


def menu():
    print("1) Ввод данных.")
    print("2) Просмотр всех данных.")
    print("3) Вывод данных по ключу.")
    print("4) Удаление данных по ключу.")
    print("5) Поиск информации о людях, родившихся сегодня.")
    print("6) Поиск информайии о людях, родившихся под введенным знаком зодиака.")
    print("7) Выход.")


zodiac_sing = defaultdict(dict)


def input_data(d):
    n = int(input("Сколько элементов хотите ввести -> "))
    for _ in range(n):
        initial = input("Введите ФИО -> ").strip()
        user_date = input("Введите дату рождения в формате ДД ММ -> ").strip()
        zodiac = input("Введите знак зодиака -> ").strip()

        d[initial][user_date] = zodiac
        print("Данные сохранены!\n")


def print_data(d):
    if d:
        for k, dv in d.items():
            for bd, zz in dv.items():
                print(f"ФИО: {k}\nДата рождения: {bd}\nЗнак зодиака: {zz}\n")
    else:
        print("Данных нет.")


def print_by_key(d):
    if d:
        need_key = input("Введите ФИО для поиска -> ")
        if need_key in d.keys():
            if d[need_key]:
                for k, v in d[need_key].items():
                    print(f"ФИО: {need_key}\nДата рождения: {k}\nЗнак зодиака: {v}")
        else:
            print("Такого пользователя нет.")
    else:
        print("Данных нет.")


def delite_by_key(d):
    if d:
        need_key = input("Введите ФИО для удаления информации -> ")
        if need_key in d.keys():
            d[need_key] = {}
            print("Данные удалены.")
        else:
            print("Такого пользователя нет.")
    else:
        print("Данных нет.")

# {ФИО:{ДР: знак}}
def search_by_today(d):
    if d:
        today_date = date.today()
        for fio, vd in d.items():
            for bd, zz in vd.items():
                user_date = bd.split()
                if today_date.day == user_date[0] and today_date.month == user_date[1]:
                    print(f"ФИО: {fio}\nДата рождения: {bd}\nЗнак зодиака: {zz}")
    else:
        print("Данных нет.")


while True:
    menu()
    user_choice = int(input("Введите пункт меню -> "))
    while user_choice not in list(range(1, 8)):
        user_choice = int(input("Такого пункта нет, попробуйте еще раз -> "))

    match user_choice:
        case 1:
            input_data(zodiac_sing)

        case 2:
            print_data(zodiac_sing)

        case 3:
            print_by_key(zodiac_sing)

        case 4:
            delite_by_key(zodiac_sing)

        case 5:
            search_by_today(zodiac_sing)

        case 7:
            print("Пока!")
            break

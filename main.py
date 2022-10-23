num1 = int(input("Ведите число 1"))
num2 = int(input("Ведите число 2"))


while True:
    numanswer = None
    print("Ведите 1 для того чтоб найти суму чисел\nВедите 2 для того чтоб нйати разницу чисел\nВедите 3 для того чтоб нйати произведение чисел\nВедите 4 для того чтоб найти частное чисел\nВедите 5 для замены чисел\nВедите 0 для выхода")
    answer = input("Ведите номер операцыи")

    if answer == '1':
        numanswer = num1 + num2
        print(f"Результат {numanswer}")
    elif answer == '2':
        numanswer = num1 - num2
        print(f"Результат {numanswer}")
    elif answer == '3':
        numanswer = num1 * num2
        print(f"Результат {numanswer}")
    elif answer == '4':
        if num1 == 0:
            print("НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ!!! Пажалуйста выбирите 5 и перезапишыте число 1")
            continue
        if num2 == 0:
            print("НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ!!! Пажалуйста выбирите 5 и перезапишыте число 2")
            continue
        numanswer = num1 // num2
        print(f"Результат {numanswer}")
    elif answer == '5':
        num1 = int(input("Ведите новое число 1"))
        num2 = int(input("Ведите новое число 2"))
        numanswer = None
    elif answer == '0':
        print("Досвидос амигос")
        break
    else:
        print("Операцыи под даным номером нет")


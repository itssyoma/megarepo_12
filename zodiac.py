# Запрос дня и месяца рождения
day = int(input("Введите день рождения: "))
month = input("Введите месяц рождения (название): ")

# Определение знака зодиака
if month == "январь":
    if day < 20:
        sign = "Козерог"
    else:
        sign = "Водолей"
elif month == "февраль":
    if day < 19:
        sign = "Водолей"
    else:
        sign = "Рыбы"
elif month == "март":
    if day < 21:
        sign = "Рыбы"
    else:
        sign = "Овен"
elif month == "апрель":
    if day < 20:
        sign = "Овен"
    else:
        sign = "Телец"
elif month == "май":
    if day < 21:
        sign = "Телец"
    else:
        sign = "Близнецы"
elif month == "июнь":
    if day < 21:
        sign = "Близнецы"
    else:
        sign = "Рак"
elif month == "июль":
    if day < 23:
        sign = "Рак"
    else:
        sign = "Лев"
elif month == "август":
    if day < 23:
        sign = "Лев"
    else:
        sign = "Дева"
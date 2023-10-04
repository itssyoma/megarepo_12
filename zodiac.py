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
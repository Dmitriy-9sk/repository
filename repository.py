temperature = float(input("Температура:"))
is_rainy = input("Есть осадки? (да/нет): ") == 'да'
is_raining_heavily = input("сильно ли дождит? (да/нет): ") == 'да' if is_rainy else False

if 30 > temperature > 20:
    if is_rainy:
        otvet = "футболка, шорты и дождевик"
    else:
        otvet = "футболка и шорты"
else:
    if temperature > 0:
        otvet = 'пальто, резиновые сапоги' if is_raining_heavily else "пальто и джинсы"
    else:
        otvet = "пуховик"

print(otvet)
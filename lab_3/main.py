import math

# 4. Функція для введення числа у діапазоні [a, b]
def input_number_in_range(a, b):
    while True:
        try:
            number = float(input(f"Введіть число у діапазоні [{a}, {b}]: "))
            if a <= number <= b:
                return number
            print("Число поза діапазоном. Спробуйте ще раз.")
        except ValueError:
            print("Неправильний формат. Спробуйте ще раз.")

# 5. Функція для введення коефіцієнтів квадратного рівняння
def input_quadratic_coefficients():
    while True:
        try:
            a = int(input("Введіть коефіцієнт a (a ≠ 0): "))
            if a == 0:
                print("Коефіцієнт a не може бути 0. Спробуйте ще раз.")
                continue
            b = int(input("Введіть коефіцієнт b: "))
            c = int(input("Введіть коефіцієнт c: "))
            return a, b, c
        except ValueError:
            print("Неправильний формат. Спробуйте ще раз.")

# 6. Функція для введення коефіцієнтів рівняння прямої ax + by + c = 0
def input_linear_coefficients():
    while True:
        try:
            a = int(input("Введіть коефіцієнт a: "))
            b = int(input("Введіть коефіцієнт b: "))
            if a == 0 and b == 0:
                print("Коефіцієнти a та b не можуть бути нульовими одночасно. Спробуйте ще раз.")
                continue
            c = int(input("Введіть коефіцієнт c: "))
            return a, b, c
        except ValueError:
            print("Неправильний формат. Спробуйте ще раз.")

# 7. Функція для введення координат точки
def input_point_coordinates():
    while True:
        try:
            x = float(input("Введіть координату x: "))
            y = float(input("Введіть координату y: "))
            return x, y
        except ValueError:
            print("Неправильний формат. Спробуйте ще раз.")

# 8. Функція для розв'язку квадратного рівняння
def solve_quadratic_equation():
    try:
        a, b, c = input_quadratic_coefficients()
        print(f"Рівняння: {a}x^2 + {b}x + {c} = 0")
        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            print(f"Розв'язки: x1 = {x1}, x2 = {x2}")
            return x1, x2
        elif discriminant == 0:
            x = -b / (2*a)
            print(f"Розв'язок: x = {x}")
            return x,
        else:
            print("Рівняння не має дійсних розв'язків.")
            return None
    except ValueError:
        print("Неправильний формат. Спробуйте ще раз.")
    except ZeroDivisionError:
        print("Помилка: ділення на нуль.")

# 9. Функція для введення додатного дійсного числа
def input_positive_real_number():
    while True:
        try:
            number = float(input("Введіть додатне число: "))
            if number > 0:
                return number
            print("Число має бути додатним. Спробуйте ще раз.")
        except ValueError:
            print("Неправильний формат. Спробуйте ще раз.")

# 10. Функція для порівняння котангенсів
def compare_cotangents(x, y):
    try:
        if math.tan(x) == 0 or math.tan(y) == 0:
            return "Невизначено (тангенс дорівнює нулю)"
        
        cot_x = 1 / math.tan(x)
        cot_y = 1 / math.tan(y)
        
        if cot_x > cot_y:
            res = ">"
        elif cot_x < cot_y:
            res = "<"
        else:
            res = "="
        
        return f"Котангенс {cot_x} {res} {cot_y}"    
        
    except ZeroDivisionError:
        return "Невизначено (ділення на нуль)"

# 11. Функція для обчислення площі трикутника за довжинами сторін
def triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print("Трикутник з такими сторонами не існує.")
        return None
    
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Завдання 4: 
num_in_range = input_number_in_range(1, 10)
print(f"Введене число: {num_in_range}")

# Завдання 5: 
a, b, c = input_quadratic_coefficients()
print(f"Коефіцієнти квадратного рівняння: a={a}, b={b}, c={c}")
print(f"{a}x^2 + {b}x + {c} = 0")

# Завдання 6: 
a, b, c = input_linear_coefficients()
print(f"Коефіцієнти рівняння прямої: a={a}, b={b}, c={c}")
print(f"{a}x + {b}y + {c} = 0")

# Завдання 7: 
x, y = input_point_coordinates()
print(f"Введена точка: ({x}, {y})")

# Завдання 8: 
solve_quadratic_equation() 

# Завдання 9: 
positive_number = input_positive_real_number()
print(f"Введене додатне число: {positive_number}")

# Завдання 10: 
x = float(input("Введіть перший кут (у радіанах): "))
y = float(input("Введіть другий кут (у радіанах): "))
comparison_result = compare_cotangents(x, y)
print(f"Результат порівняння котангенсів: {comparison_result}")

# Завдання 11:
a = input_positive_real_number()
b = input_positive_real_number()
c = input_positive_real_number()
area = triangle_area(a, b, c)
if area:
    print(f"Площа трикутника: {area}")


#########Додати в словник:
def add_to_dict(dict, key, value):
    dict[key] = value
    print(f"Додано: {key} -> {value}")

dict = {"green": "зелений" }
add_to_dict(my_dict, "red", "червоний")
print(my_dict)

########### Удалити
def remove_from_dict(dict, key):
    if key in dict:
        value = dict.pop(key)
        print(f"Видалено: {key} -> {value}")
    else:
        print("Ключ не знайдено")

remove_from_dict(dict, "green")
print(my_dict)

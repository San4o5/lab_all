import math

def reverse_number(n):
    return int(str(n)[::-1])

def count_digit(n, d):
    return str(n).count(str(d))

def evaluate_expression(expression):
    return eval(expression)

def binary_search(f, a, b, tol=1e-6):
    while b - a > tol:
        mid = (a + b) / 2  
        if f(a) * f(mid) <= 0:
            b = mid  
        else:
            a = mid  
    return (a + b) / 2 

def square_digits(n):
    return int("".join(str(int(d) ** 2) for d in str(n)))

def replace_sixes_with_twos(n):
    return int(str(n).replace('6', '2'))

def remove_zeros(n):
    return int(str(n).replace('0', ''))

def remove_every_second_digit(n):
    return int(str(n)[::2])

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def count_fib_calls(n, calls=0):
    calls += 1
    if n <= 1:
        return n, calls
    left, calls = count_fib_calls(n - 1, calls)
    right, calls = count_fib_calls(n - 2, calls)
    return left + right, calls

def smallest_factorial(a):
    n, fact = 1, 1
    while fact < a:
        n += 1
        fact *= n
    return n

def largest_factorial(a):
    n, fact = 1, 1
    while fact * (n + 1) <= a:
        n += 1
        fact *= n
    return n

def integer_log(n, m):
    if n <= 1 or m <= 0:
        return "Некоректні вхідні дані"
    return math.floor(math.log(m, n))

def digit_info(n, d):
    str_n = str(n)
    return {
        "кількість цифр": len(str_n),
        "цифра зустрічається": str(d) in str_n,
        "кількість входжень": str_n.count(str(d)),
        "старша цифра": int(str_n[0]),
        "мінімальна цифра": min(map(int, str_n)),
        "максимальна цифра": max(map(int, str_n))
    }

def main():
    n = int(input("Введіть число n: "))
    d = int(input("Введіть цифру d (Кількість входжень цифри у числі n): "))
    expression = input("Введіть арифметичний вираз: ")
    a, b = map(float, input("Введіть a і b для методу половинного ділення: ").split())
    fact_a = int(input("Введіть a для факторіалу: "))
    log_n, log_m = map(int, input("Введіть n та m для логарифму: ").split())
    
    print(f"\nОбернене число: {reverse_number(n)}")
    print(f"Кількість входжень цифри {d} у числі {n}: {count_digit(n, d)}")
    print(f"Значення виразу {expression}: {evaluate_expression(expression)}")
    print(f"Корінь рівняння методом половинного ділення: {binary_search(lambda x: x**2 - 2, a, b)}")
    print(f"Число, утворене квадратами цифр {n}: {square_digits(n)}")
    print(f"Число після заміни 6 → 2: {replace_sixes_with_twos(n)}")
    print(f"Число після видалення нулів: {remove_zeros(n)}")
    print(f"Число після видалення кожної другої цифри: {remove_every_second_digit(n)}")
    print(f"Найменше n, для якого n! ≥ {fact_a}: {smallest_factorial(fact_a)}")
    print(f"Найбільше n, для якого n! ≤ {fact_a}: {largest_factorial(fact_a)}")
    print(f"[log_{log_n} {log_m}]: {integer_log(log_n, log_m)}")
    
    digit_stats = digit_info(n, d)
    for key, value in digit_stats.items():
        print(f"{key}: {value}")
    
    fib_number, calls = count_fib_calls(n)
    print(f"{n}-те число Фібоначчі: {fib_number}")
    print(f"Кількість рекурсивних викликів для {n}-го числа Фібоначчі: {calls}")

if __name__ == "__main__":
    main()

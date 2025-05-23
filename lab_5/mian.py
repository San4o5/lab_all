
# завдання 1
MIN_VALUE = 0
MAX_VALUE = 1

x = float(input(f'Input a float from [{MIN_VALUE};{MAX_VALUE}]: '))
if x < MIN_VALUE or x > MAX_VALUE:
    raise ValueError(f'Your number not in [{MIN_VALUE};{MAX_VALUE}]')

# завдання 2
APPROX_PI = 3
FOUR = 4
THREE = 3
TWO = 2

radius = 2.56
length = TWO * APPROX_PI * radius
square = APPROX_PI * radius * radius
volume = (FOUR / THREE) * APPROX_PI * radius ** THREE

# завдання 3
# Умова
def f(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return f(n - 1) + f(n - 2)

# а) Яку загальновідому послідовність обчислює ця функція?
#Це послідовність Фібоначчі.

# б) Яка часова складність наведеної функції відносно значення n?
#Часова складність — O(2ⁿ), бо для кожного виклику функція викликається двічі (для n-1 і n-2).

# в) Якщо рахувати складність відносно розміру вхідних даних?
#Якщо розмір вхідних даних — це кількість біт для представлення n, то складність буде експоненційною відносно кількості біт, тобто також дуже велика.

# г) Яка просторова складність наведеної функції відносно n?
#Просторова складність — O(n) через глибину рекурсії до n рівнів.

# д) А якщо врахувати специфіку об'єктної моделі мови Python?
#У Python кожен рекурсивний виклик створює окремий запис у стеку викликів, тому реально витрачається більше пам'яті через службову інформацію про виклики
# функцій (адреса повернення, локальні змінні тощо).

#е) Яка просторова складність наведеної функції відносно розміру вхідних даних?
#Аналогічно, O(n) просторової складності через рекурсивний стек.

# ж) Чи можна цю задачу розв'язати швидше та з меншими витратами пам'яті?
#Так! Можна:
#    Ітераційно:
#        Часова складність: O(n)
#        Просторова складність: O(1)
# приклад
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

print(f(n = 13))
print(fibonacci_iterative(n = 13))

# Завдання 4
#Алгоритм                  | Кількість порівнянь             | Кількість присвоювань
#Вибором (Selection Sort)  | ~n²/2 порівнянь                 | ~n присвоювань
#Вставкою (Insertion Sort) | ~n²/4 порівнянь (у середньому)  | ~n²/4 присвоювань
#Бульбашкою (Bubble Sort)  | ~n²/2 порівнянь                 | ~n²/2 присвоювань
#Пірамідою (Heap Sort)     | ~n log n порівнянь              | ~n log n присвоювань
#Злиттям (Merge Sort)      | ~n log n порівнянь              | ~n log n присвоювань
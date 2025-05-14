# Завдання 1
# а)
numbers = [i for i in range(2, 20)][:3]
print("1a:", numbers)

# б)
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print("1b:", squares)

# в)
reverse_squares = []
for i in range(10, -1, -1):
    reverse_squares.append(i ** 2)
print("1c:", reverse_squares)

# г)
filtered_numbers = []
for i in range(101):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        filtered_numbers.append(i)
print("1d:", filtered_numbers)

# Завдання 2
# а)
gen_a = (i ** 2 for i in range(1, 11))
print("2a:", list(gen_a))

# б)
gen_b = (i ** 2 for i in range(10, -1, -1))
print("2b:", list(gen_b))

# в)
gen_c = (i for i in range(101) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0)
print("2c:", list(gen_c))

# Завдання 3
# а)
gen_3a = (x for x in range(1000) if x % 2 == 0)
print("3a:", list(gen_3a))

# б)
gen_3b = (x for x in range(1000) if x % 2 != 0 and x % 3 != 0 and x % 5 != 0)
print("3b:", list(gen_3b))

# в)
threshold = 500
gen_3v = (x for x in range(1000) if x > threshold)
print("3v:", list(gen_3v))

# г)
sequence = range(-100, 100)
gen_3g = (x for x in sequence if x > 0)
print("3g:", list(gen_3g))

# ґ)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

gen_3d = (x for x in range(2, 1000) if is_prime(x))
print("3d:", list(gen_3d))

# д)
gen_3e = (x for x in range(1000) if int(x ** 0.5) ** 2 == x)
print("3e:", list(gen_3e))

# Завдання 4
sequence = [1, 2.5, 'abc', 3, -4, 7.1, 8]

# а)
ints = []
for x in sequence:
    if isinstance(x, int):
        ints.append(x)
print("4a:", ints)

# б)
floats = []
for x in sequence:
    if isinstance(x, float):
        floats.append(x)
print("4b:", floats)

# в)
non_floats = []
for x in sequence:
    if not isinstance(x, float):
        non_floats.append(x)
print("4v:", non_floats)

# г)
non_strs = []
for x in sequence:
    if not isinstance(x, str):
        non_strs.append(x)
print("4g:", non_strs)

# Завдання 5
sequence = list(range(1, 21))
length = len(sequence)
half = length // 2
third = length // 3

# а)
first_half = sequence[:half + (length % 2)]
print("5a:", first_half)

# б)
first_half_excl_center = sequence[:half]
print("5b:", first_half_excl_center)

# в)
first_third = sequence[:third]
print("5v:", first_third)

# г)
second_half = sequence[half:]
print("5g:", second_half)

# ґ)
second_half_excl_center = sequence[half + (length % 2):]
print("5d:", second_half_excl_center)

# д)
second_third = sequence[third:2 * third]
print("5e:", second_third)

# е)
last_third = sequence[2 * third:]
print("5e:", last_third)

# є)
every_third_reversed = []
for i in range(length - 1, -1, -3):
    every_third_reversed.append(sequence[i])
print("5je:", every_third_reversed)

# Завдання 6
s = [1, 2, 3, 2, 4, 5, 1, 6]
unique_elements = list(set(s))
print("6:", unique_elements)

# Завдання 7
text = "abc123def4567gh89"
digit_count = {}
for ch in text:
    if ch.isdigit():
        if ch in digit_count:
            digit_count[ch] += 1
        else:
            digit_count[ch] = 1
print("7:", digit_count)

# Завдання 8
s = [4, 2, 3, 4, 5, 4, 6]
el = 4
positions = []
for idx in range(len(s)):
    if s[idx] == el:
        positions.append(idx)
print("8:", positions)

#############################################

# Завдання 9
sequence = [0, -5, 3, -1, 9, 2]
positive = [x for x in sequence if x > 0]
min_positive = min(positive) if positive else None
print("9:", min_positive)

# Завдання 10
sequence = [1, 2, 3, 2, 4, 2]
sum_even_mult = sum(x * sequence.count(x) for x in set(sequence) if x % 2 == 0)
print("10:", sum_even_mult)

# Завдання 11
sequence = [1, 2, 3, 2, 1, 2]
sum_mult = sum(x * sequence.count(x) for x in set(sequence))
print("11:", sum_mult)

# Завдання 12
sequence = [10, 20, 30, 40, 50, 60]

sum_even_idx = 0
for i in range(0, len(sequence), 2):
    sum_even_idx += sequence[i]
print("12a:", sum_even_idx)

sum_odd_idx = 0
for i in range(1, len(sequence), 2):
    sum_odd_idx += sequence[i]
print("12b:", sum_odd_idx)

# Завдання 13
sequence = [1, 2, 3, 4]
all_positive = all(x > 0 for x in sequence)
print("13a:", all_positive)

all_integers = all(isinstance(x, int) for x in sequence)
print("13b:", all_integers)

# Завдання 14
sequence = [14, 21, 28]
all_div_7 = all(x % 7 == 0 for x in sequence)
print("14a:", all_div_7)

threshold = 10
all_gt = all(x > threshold for x in sequence)
print("14b:", all_gt)

all_squares = all(int(x ** 0.5) ** 2 == x for x in sequence)
print("14v:", all_squares)

all_primes = all(is_prime(x) for x in sequence)
print("14g:", all_primes)

######################################3

# 15. Вирази для перевірки, чи послідовність містить:
sequence = [1, -5, 7, 13, 4, 17, 8]  # приклад

# a) число 7
contains_7 = 7 in sequence

# b) від’ємні числа
contains_negative = any(x < 0 for x in sequence)

# c) хоча б одне число, що ділиться на 13
divisible_by_13 = any(x % 13 == 0 for x in sequence)

# d) хоча б одне просте число
contains_prime = any(is_prime(x) for x in sequence)

# 16
sequence_length = len(sequence)

# 17
is_stationary = all(x == sequence[0] for x in sequence)

# 18
def is_majoring(a, b):
    if len(a) != len(b):
        return False

    for x, y in zip(a, b):
        if x < y:
            return False

    return True


# 19
def compare(v1, v2):
    if len(v1) != len(v2):
        return None
    if v1 == v2:
        return -1
    elif all(x <= y for x, y in zip(v1, v2)):
        return 0
    elif all(x >= y for x, y in zip(v1, v2)):
        return 1
    else:
        return None

# 20
def custom_sort(lst):
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    return evens + odds

# Приклад використання
example_list = [5, 2, 7, 8, 1, 4]
sorted_list = custom_sort(example_list)

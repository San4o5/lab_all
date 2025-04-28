# завдання 4а
def create_list():
    result = []
    try:
        while True:
            value = input("Введіть ціле число: ")
            result.append(int(value))
    except (ValueError, EOFError):
        return result
    
# завдання 4б
def create_list_with_none():
    result = []
    try:
        while True:
            value = input("Введіть ціле число: ")
            result.append(int(value))
    except ValueError:
        return None
    except EOFError:
        return result

# завдання 4в
def create_list_with_runtimeerror():
    result = []
    try:
        while True:
            value = input("Введіть ціле число: ")
            result.append(int(value))
    except ValueError:
        raise RuntimeError("Введено нечислове значення!")
    except EOFError:
        return result

# завдання 4г
def create_list_ignore_non_numbers():
    result = []
    try:
        while True:
            value = input("Введіть ціле число: ")
            try:
                result.append(int(value))
            except ValueError:
                pass  
    except EOFError:
        return result

# завдання 5а
def fill_existing_list(lst):
    try:
        while True:
            value = input("Введіть ціле число: ")
            lst.append(int(value))
    except ValueError:
        return False
    except EOFError:
        return True

# завдання 5б
def fill_existing_list_safe(lst):
    temp = []
    try:
        while True:
            value = input("Введіть ціле число: ")
            temp.append(int(value))
    except ValueError:
        return False  # lst залишається незмінним
    except EOFError:
        lst.extend(temp)  # тільки якщо все ок, копіюємо в lst
        return True

# завдання 6а
def create_list_n_numbers(n):
    result = []
    try:
        for _ in range(n):
            value = input("Введіть ціле число: ")
            result.append(int(value))
    except ValueError:
        raise RuntimeError("Введено нечислове значення!")
    return result

# завдання 6б
def create_list_n_numbers_ignore(n):
    result = []
    while len(result) < n:
        try:
            value = input("Введіть ціле число: ")
            result.append(int(value))
        except ValueError:
            pass  
    return result

# завдання 7
def create_list_of_type(desired_type):
    result = []
    try:
        while True:
            value = input(f"Введіть значення типу {desired_type.__name__}: ") #__name__ — об'єкт типу, який повертає назву у вигляді рядка
            result.append(desired_type(value))
    except ValueError:
        raise RuntimeError(f"Введено значення, що не можна перетворити у {desired_type.__name__}!")
    except EOFError:
        return result

# завдання 8
def add_unique_element(lst, element):
    if element in lst:
        return False
    lst.append(element)
    return True

# завдання 9
def create_list_n_unique_numbers(n):
    result = []
    try:
        while len(result) < n:
            value = int(input("Введіть ціле число: "))
            if value not in result:
                result.append(value)
    except ValueError:
        raise RuntimeError("Введено нечислове значення!")
    return result

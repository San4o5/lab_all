import math
import sys

def show_help():
    print("Допустимі аргументи:")
    print("  pi    - вивести число π з 4 знаками після крапки")
    print("  e     - вивести число e з 6 знаками після крапки")
    print("  help  - показати довідку")

def main():
    # Перевіряємо кількість аргументів командного рядка.
    if len(sys.argv) != 2:
        print("Помилка: очікується один аргумент командного рядка.\n")
        show_help()
        return

    # sys.argv[0] - це ім'я файлу
    # sys.argv[1] — це перший переданий користувачем аргумент
    command = sys.argv[1]

    if command == "pi":
        print(f"{math.pi:.4f}")
    elif command == "e":
        print(f"{math.e:.6f}")
    elif command == "help":
        show_help()
    else:
        print(f"Невідома команда: {command}\n")
        show_help()

if __name__ == "__main__":
    main()

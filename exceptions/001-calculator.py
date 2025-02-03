class ZeroNegativePowerException(Exception):
    ...


def get_user_input() -> list[int, int] | None:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    num1, num2 = int(num1), int(num2)
    return num1, num2


def add(num1: int, num2: int) -> int:
    return num1 + num2


def subtract(num1: int, num2: int) -> int:
    return num1 - num2


def multiply(num1: int, num2: int) -> int:
    return num1 * num2


def divide(num1: int, num2: int) -> float:
    return num1 / num2


def power(num1: int, num2: int) -> int:
    if num1 == 0 and num2 < 0:
        raise ZeroNegativePowerException
    return num1 ** num2


operations = {
    "1": add,
    "2": subtract,
    "3": multiply,
    "4": divide,
    "5": power,
}


def main():
    print("1. Add\n2.Subtract\n3. Multiply\n4. Divide\n5. Power\n0. Exit")
    menu_choice = input("$> ")

    if menu_choice == "0":
        print("Bye!")
        return False
    try:
        operation = operations[menu_choice]
        num1, num2 = get_user_input()
        result = operation(num1, num2)
        print(f"Result: {result}\n")
    except KeyError:
        print("Invalid menu option.")
    except ValueError:
        print("Entered numbers invalid.")
    except ZeroDivisionError:
        print("Division by zero is not supported.")
    except ZeroNegativePowerException:
        print("Power of zero to negative is not supported.")
    
    return True




if __name__ == "__main__":
    continue_exec = True
    while continue_exec:
        continue_exec = main()
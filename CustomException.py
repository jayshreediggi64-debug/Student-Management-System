# Custom Exception
class InvalidOrderError(Exception):
    pass

try:
    # Input three integers
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    # Check condition
    if not (a > b and b > c):
        raise InvalidOrderError("The condition a > b > c is not satisfied.")

    # Ask for mood
    mood = input("Enter your mood (happy/sad): ").strip().lower()

    if mood == "happy":
        print("OK")
    elif mood == "sad":
        print("Need counseling")
    else:
        print("Invalid mood entered.")

except InvalidOrderError as e:
    print("InvalidOrderError:", e)

except ValueError:
    print("Error: Please enter valid integer values.")

except Exception as e:
    print("An unexpected error occurred:", e)
# ------------------------------------------------------------
# Manejo de funciones en Python
# ------------------------------------------------------------
# Name: Gerardo Lizarriturri Elizondo
# Student ID: 2530517
# Group: IM 1-2
# ------------------------------------------------------------
# START OF CODE
# ------------------------------------------------------------

# ------------------------------------------------------------
# Problem : 1 - Rectangle area and perimeter
# ------------------------------------------------------------

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)


try:
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    if width > 0 and height > 0:
        area = calculate_area(width, height)
        perimeter = calculate_perimeter(width, height)

        print("Area:", area)
        print("Perimeter:", perimeter)
    else:
        print("Error: invalid input")

except ValueError:
    print("Error: invalid input")

# ------------------------------------------------------------
# Problem : 2 - Grade classifier
# ------------------------------------------------------------

def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


try:
    score = float(input("Enter score (0-100): "))

    if 0 <= score <= 100:
        letter = classify_grade(score)
        print("Score:", score)
        print("Category:", letter)
    else:
        print("Error: invalid input")

except ValueError:
    print("Error: invalid input")

# ------------------------------------------------------------
# Problem : 3 - List statistics function (min, max, average)
# ------------------------------------------------------------

def summarize_numbers(numbers_list):
    info = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return info


numbers_text = input("Enter numbers separated by commas: ").strip()

if numbers_text == "":
    print("Error: invalid input")
else:
    try:
        parts = numbers_text.split(",")
        numbers_list = []

        for p in parts:
            num = float(p)
            numbers_list.append(num)

        if len(numbers_list) == 0:
            print("Error: invalid input")
        else:
            stats = summarize_numbers(numbers_list)
            print("Min:", stats["min"])
            print("Max:", stats["max"])
            print("Average:", stats["average"])

    except ValueError:
        print("Error: invalid input")

# ------------------------------------------------------------
# Problem : 4 - Apply discount list (pure function)
# ------------------------------------------------------------

def apply_discount(prices_list, discount_rate):
    new_list = []
    for price in prices_list:
        new_price = price * (1 - discount_rate)
        new_list.append(new_price)
    return new_list


prices_text = input("Enter prices separated by commas: ").strip()

if prices_text == "":
    print("Error: invalid input")
else:
    try:
        parts = prices_text.split(",")
        prices_list = []

        for p in parts:
            price = float(p)
            if price <= 0:
                raise ValueError
            prices_list.append(price)

        if len(prices_list) == 0:
            print("Error: invalid input")
        else:
            try:
                discount_rate = float(input("Enter discount rate (0 to 1): "))
                if discount_rate < 0 or discount_rate > 1:
                    print("Error: invalid input")
                else:
                    discounted = apply_discount(prices_list, discount_rate)
                    print("Original prices:", prices_list)
                    print("Discounted prices:", discounted)
            except ValueError:
                print("Error: invalid input")

    except ValueError:
        print("Error: invalid input")

# ------------------------------------------------------------
# Problem : 5 - Greeting function with default parameters
# ------------------------------------------------------------

def greet(name, title=""):
    if title == "":
        full_name = name
    else:
        full_name = title + " " + name
    return f"Hello, {full_name}!"


name = input("Enter name: ").strip()

if name == "":
    print("Error: invalid input")
else:
    title = input("Enter title (optional): ").strip()
    # title can be empty, so no strict validation needed
    message = greet(name, title)
    print("Greeting:", message)

# ------------------------------------------------------------
# Problem : 6 - Factorial function
# ------------------------------------------------------------

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


try:
    n_text = input("Enter an integer n: ").strip()

    # Validate integer
    if not n_text.lstrip("-").isdigit():
        print("Error: invalid input")
    else:
        n = int(n_text)

        # Validations
        if n < 0 or n > 20:
            print("Error: invalid input")
        else:
            value = factorial(n)
            print("n:", n)
            print("Factorial:", value)

except:
    print("Error: invalid input")

# --------------------------------------------------
# REFERENCES
# --------------------------------------------------
# 1) Python Official Documentation – Functions:
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
#
# 2) W3Schools – Python Functions Tutorial:
#    https://www.w3schools.com/python/python_functions.asp
#
# 3) Real Python – Defining and Using Functions:
#    https://realpython.com/defining-your-own-python-function/
#
# 4) GeeksforGeeks – Python Functions:
#    https://www.geeksforgeeks.org/python-functions/
#
# 5) Programiz – Python Function Examples:
#    https://www.programiz.com/python-programming/function
#
# 6) TutorialsPoint – Python Functions:
#    https://www.tutorialspoint.com/python/python_functions.htm
#
# 7) Stack Overflow – Common Questions About Python Function Design:
#    https://stackoverflow.com/questions/tagged/python-functions
# --------------------------------------------------
# END OF CODE
# --------------------------------------------------

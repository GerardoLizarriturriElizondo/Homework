# ------------------------------------------------------------
# Fibonacci Series with Python
# ------------------------------------------------------------
# Name: Gerardo Lizarriturri Elizondo
# Student ID: 2530517
# Group: IM 1-2
# ------------------------------------------------------------
# PROBLEM: Fibonacci series generator
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

# Read input
user_input = input("Enter the number of terms: ")

# Input validation
try:
    n = int(user_input)

    if n < 1 or n > 50:
        print("Error: invalid input")
        exit()

except:
    print("Error: invalid input")
    exit()

# Fibonacci calculation
first = 0
second = 1

# Special cases
if n == 1:
    print("Fibonacci series: 0")
    exit()
elif n == 2:
    print("Fibonacci series: 0 1")
    exit()

# Generate the series for n >= 3
fibonacci_list = [first, second]

for _ in range(3, n + 1):
    next_term = first + second
    fibonacci_list.append(next_term)
    first = second
    second = next_term

# Output
print("Fibonacci series:", *fibonacci_list)

# ------------------------------------------------------------
# REFERENCES
# ------------------------------------------------------------
# 1) Python Official Documentation – "for Statements"
#    https://docs.python.org/3/tutorial/controlflow.html#for-statements
#
# 2) Python Official Documentation – "while Statements"
#    https://docs.python.org/3/tutorial/controlflow.html#the-while-statement
#
# 3) GeeksforGeeks – "Program for Fibonacci Numbers in Python"
#    https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers/
#
# 4) W3Schools – "Python For Loops"
#    https://www.w3schools.com/python/python_for_loops.asp
#
# 5) TutorialsPoint – "Python Fibonacci Series"
#    https://www.tutorialspoint.com/python-program-to-print-fibonacci-series
# ------------------------------------------------------------
# END OF CODE
# ------------------------------------------------------------

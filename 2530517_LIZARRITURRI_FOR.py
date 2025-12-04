# Problema 1

n_text = input("Ingrese n: ").strip()

try:
    n = int(n_text)
    if n < 1:
        print("Error: invalid input")
        exit()
except ValueError:
    print("Error: invalid input")
    exit()

total_sum = 0
even_sum = 0

for i in range(1, n + 1):
    total_sum += i
    if i % 2 == 0:
        even_sum += i

print("Sum 1..n:", total_sum)
print("Even sum 1..n:", even_sum)

# Problema 2

base_text = input("Ingrese base: ").strip()
m_text = input("Ingrese m: ").strip()

try:
    base = int(base_text)
    m = int(m_text)
    if m < 1:
        print("Error: invalid input")
        exit()
except ValueError:
    print("Error: invalid input")
    exit()

for i in range(1, m + 1):
    print(f"{base} x {i} = {base * i}")

# Problema 3

sentinel_value = -1
count = 0
total = 0.0

while True:
    number_text = input("Ingrese un número (-1 para terminar): ").strip()
    try:
        number = float(number_text)
    except ValueError:
        print("Error: invalid number")
        continue
    if number == sentinel_value:
        break
    total += number
    count += 1

if count == 0:
    print("Error: no data")
else:
    average = total / count
    print("Count:", count)
    print("Average:", average)

# Problema 4

CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    user_password = input("Ingrese la contraseña: ").strip()
    attempts += 1
    if user_password == CORRECT_PASSWORD:
        print("Login success")
        break
else:
    print("Account locked")

# Problema 5

counter = 0

while True:
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")
    
    option_text = input("Seleccione una opción: ").strip()
    try:
        option = int(option_text)
    except ValueError:
        print("Error: invalid option")
        continue

    if option == 0:
        print("Bye!")
        break
    elif option == 1:
        print("Hello!")
    elif option == 2:
        print("Counter:", counter)
    elif option == 3:
        counter += 1
        print("Counter incremented")
    else:
        print("Error: invalid option")

# Problema 5

n_text = input("Ingrese el número de filas: ").strip()

try:
    n = int(n_text)
    if n < 1:
        print("Error: invalid input")
        exit()
except ValueError:
    print("Error: invalid input")
    exit()

for i in range(1, n + 1):
    print("*" * i)

for i in range(n, 0, -1):
    print("*" * i)

'''
Nombre: Gerardo Lizarriturri Elizondo
Matricula: 2530517
Grupo: IM 1-2
'''


'''
Primer Ejercicio
name = input("What's your name? ")

if name.strip() != "" and len(name.split()) >= 2:
    palabras = name.strip().split()
    iniciales = "".join(p[0].upper() for p in palabras)
    
    print(name.title())
    print(iniciales)
else:
    print("Write your name correctly")
'''

'''
Segundo Problema
email = input("Write your email? ")
atsign = 0
position = email.find("@")

for o in email.strip():
    if o == "@":
        atsign = atsign + 1

if atsign==1 and "." in email.strip()[position+1:]:
    print("Valid email")
    print(email[position+1:])
else:
    print("not a valid email")
'''

'''
Tercer Ejercicio
phrase = input("Write your phrase: ")
phrase = phrase.strip().lower()
reverse= phrase[::-1]
if phrase != "" and len(phrase) >= 3:
    if phrase == reverse:
        print("Its palindrome")
    else:
        print("Its not a palindrome")
else:
    print("write an appropiate text")
'''     

'''
phrase = input("Write your phrase: ")
phrase = phrase.strip()
splitted_phrase = phrase.split()
len_1=len(splitted_phrase[0])
len_2=len(splitted_phrase[1])

if len_1>= 3 and len_2>=3:
    if len_1>len_2:
        print(f"{splitted_phrase[0]} es mas largo que {splitted_phrase[1]}")
    elif len_2>len_1:
        print(f"{splitted_phrase[1]} es mas largo que {splitted_phrase[0]}")
    else:
        print("both words have the same lenght")
else:
    print("eiter the phrase you wrote is too short, or is straight up empty")
'''
''''
password = input("Write your password: ")
upper_ = lower_ = num_ = special_character = False


for s in password:
    if s.isupper():
        upper_=True
    elif s.islower():
        lower_=True
    elif s.isdigit():
        num_=True
    elif not s.isalnum():
        special_character=True
print(upper_, lower_, num_, special_character)


if password != "":
    if len(password) < 7:
        print("Password weak")
    elif len(password)>= 8 and upper_==True and lower_==True and num_==True and special_character==True:
        print("Strong password")    
    elif len(password)>= 8 and upper_==True and lower_==True:
        print("password mid")
'''


product = input("Write the name of the product:")
price = float(input("Write the price of the product:"))

product = product.strip().lower()

product_price = f"{product}| ${price}"

if len(product_price) <30:
    product_price.ljust(30,"")
    





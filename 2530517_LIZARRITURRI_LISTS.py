'''
try:
    x1 = float(input("Ingrese x1: "))
    y1 = float(input("Ingrese y1: "))
    x2 = float(input("Ingrese x2: "))
    y2 = float(input("Ingrese y2: "))

except ValueError:
    print ("Error")
    return

punto_1 = (x1,y1)
punto_2 = (x2,y2)


distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

print("Point A:", punto_1)
print("Point B:", punto_2)
print("Distance:", distance)
print("Midpoint:", midpoint)
'''

product_dic = {
    "apple": 10,
    "banana": 20,
    "Watermelon": 30,
    
}

product = input("Write the name of the product: ").strip()
if product == "":
    print("Error: Product name cannot be empty.")
    exit


try:
    price = float(input("Write the price of the product: "))

except ValueError:
    print("Error: Invalid price input.")
    exit



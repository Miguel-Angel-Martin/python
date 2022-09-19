a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))

try:
    division = a / b
    print(division)
except ZeroDivisionError as err:
    print("Por favor ingrese valores válidos.", err)
else:
    print("Ambos valores son válidos.")
finally:
    print("¡finally!")
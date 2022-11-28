# https://youtu.be/Kp4Mvapo5kc?t=26619

### Functions ###

# Definition

def my_function():
    '''my_function'''
    print("This is a function")


my_function()
my_function()
my_function()

# Function with arguments and inputs.


def sum_two_values(first_value: int, second_value):
    '''parameters'''
    print(first_value + second_value)


sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

# Function with return


def sum_two_values_with_return(first_value, second_value):
    '''function with return'''
    my_sum = first_value + second_value
    return my_sum


my_result = sum_two_values(1.4, 5.2)
print('Fucntion without return: ', my_result)

MY_RESULT = sum_two_values_with_return(10, 5)
print('Function with return: ', MY_RESULT)

# Función con parámetros de entrada/argumentos por clave


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Moure", name="Brais")

# Función con parámetros de entrada/argumentos por defecto


def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Brais", "Moure")
print_name_with_default("Brais", "Moure", "MoureDev")

# Función con parámetros de entrada/argumentos arbitrarios


def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")

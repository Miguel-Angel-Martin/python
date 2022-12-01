'''exceptions'''
# https://youtu.be/Kp4Mvapo5kc?t=32030

### Exception Handling ###

NUMBER_ONE = 5
NUMBER_TWO = 1
NUMBER_TWO = "1"
EXCEPTION = "EXCEPTION "

# Exception base: try except

try:
    print(NUMBER_ONE + NUMBER_TWO)
    print("all works perfectly")
except TypeError as type_error:
    print("There is an "+EXCEPTION + ": " +
          str(type_error) + ".In addition operation")

try:
    print(NUMBER_ONE + NUMBER_TWO)
    print("all works perfectly 2")
except TypeError:
    print("There is some error in addition 2")
else:
    print("The execution continues correctly.")
finally:  # this sentence executing always
    print("The execution continues correctly: finally.")


try:
    print(NUMBER_ONE + NUMBER_TWO)
    print("There is some error in addition 3")
except ValueError:
    print("There is some error in addition 3 value error")
except TypeError:
    print("There is some error in addition 3 type error")


try:
    print(NUMBER_ONE + NUMBER_TWO)
    print("There is some error in addition 4")
except ValueError as error:
    print("There is some error in addition 4: ", error)
except TypeError as my_random_error_name:
    print("Error description: ", my_random_error_name)
except ArithmeticError as my_random_error_name:
    print("Error description: ", my_random_error_name)

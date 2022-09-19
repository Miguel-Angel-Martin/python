import random

days = ["Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]
temp = [30.5, 32.6, 31.8, 33.4, 29.8, 30.2, 29.9]
weekly_temp = {days: temp for (days, temp) in zip(days, temp)}
print(weekly_temp)
print("____________________________________")


customers = ["Alex", "Bob", "Carol", "Dave", "Flow", "Katie", "Nate"]
discounts_dictionary = {customer: random.randint(
    1, 100) for customer in customers}
print(discounts_dictionary)
print (discounts_dictionary.items())


print("____________________________________")
customer_10 = {customer:discount for (customer, discount) in discounts_dictionary.items() if discount<30}

print(customer_10)
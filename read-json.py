import json

JSON_data = """
{
	"tamano": "mediana",
	"precio": 15.67,
	"toppings": ["champinones", "queso extra", "pepperoni", "albahaca"],
	"cliente": {
		"nombre": "Jane Doe",
		"telefono": "455-344-234",
		"correo": "janedoe@email.com"
	}
}
"""
dict_data = json.loads(JSON_data)
print (dict_data)
print (dict_data["tamano"])
print(dict_data["cliente"]["nombre"])
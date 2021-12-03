import pprint

data = {
    'name': "Aditya Priyadarshi",
    'username': 'foxy4096',
    'website': 'https://foxy4096.github.io'
}

print('--------------------------------------------------------------------------------')

print("\nWithout pretty print\n")

print(data)

print("\nThe data is not properly formatted \n")

print('--------------------------------------------------------------------------------')

print("\nWith pretty print\n")

pprint.pprint(data)

print("\nHere the data is properly formatted\n")

# Creating the custom pprint
foxprint = pprint.PrettyPrinter(indent=5, width=15)

print("\nUsing the custom pprint we have just made now.")

foxprint.pprint(data)

print('--------------------------------------------------------------------------------')

print("\nThe pformat method will take our object and return a formatted string\n")

print("""
# formatted_data = pprint.pformat(data)

# print(formatted_data)\n""")

formatted_data = pprint.pformat(data)

print(formatted_data)

print('--------------------------------------------------------------------------------')

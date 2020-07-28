customer = {
    "name": "John smith",
    "age": 30,
    "is_verified": True
}
customer["name"] = "Jack Smith"
print(customer["name"])
print(customer.get("birthday", "Jan 1 1990"))
phone = input("Phone: ")
digits_mapping = {
    "1": "one",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
    print(output)

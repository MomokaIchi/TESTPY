# Dictionary Basics

user = {
    "name":"Alex",
    "age": 25
}

user["age"] += 1
user["city"] = "Tokyo"

print(user)

# "name": "Alex"
# "age": 26
# "city": "Tokyo"   -> not bad, but the answer is:
# {'name': 'Alex', 'age': 26, 'city': 'Tokyo'}

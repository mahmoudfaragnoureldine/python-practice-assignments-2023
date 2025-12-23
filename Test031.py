# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear ()

user = {
    "walid" : 1
}
print(user)  # {'walid': 1}
user.clear()
print(user)  # {}

print('=' * 45)

# uptate()
# => update new item in dict

member = {
    "name": "Walid"
}
print(member)  # {'name': 'Walid'}
member["age"] = 36
print(member)  # {'name': 'Walid', 'age': 36}

member.update({"country" : "Egypt"}) # you can put more than one key : value
print(member) # {'name': 'Walid', 'age': 36, 'country': 'Egypt'}

print('='  * 45)

# copy()

main = {
    "name": "Walid"
}

b = main.copy()
print(b) # {'name': 'Walid'}

main.update({"skills" : "fotball"})
print(main) # {'name': 'Walid', 'skills': 'fotball'}
print(b) # {'name': 'Walid'}

print('='  * 45)

# keys() + values()

print(main.keys())   # dict_keys(['name', 'skills'])
print(main.values()) # dict_values(['Walid', 'fotball'])








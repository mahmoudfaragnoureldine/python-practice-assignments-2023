# -------------------------------
# -- Dictionary Methods Part 2 --
# -------------------------------

# setdefault()

user = {
    "name": "Walid"
}
print(user) # {'name': 'Walid'}
print(user.setdefault("name")) # Walid
print(user) # {'name': 'Walid'}

print(user) # {'name': 'Walid'}
print(user.setdefault("age", 36)) # 36
print(user) # {'name': 'Walid', 'age': 36}

print(user) # {'name': 'Walid', 'age': 36}
print(user.setdefault("post")) # None
print(user) # {'name': 'Walid', 'age': 36, 'post': None}

print('=' *45)

# popitem()
# returns the last item add to dic

member = {
    "name": "Walid",
    "skill": "PS4"
}
print(member) # {'name': 'Walid', 'skill': 'PS4'}
member.update({"age" : 36})
print(member.popitem()) # ('age', 36)

print('='*45)

# items()
# returns all items in the dic

view = {
    "name": "Walid",
    "skill": "PS4"
}

allItems = view.items()
print(view)  #{'name': 'Walid', 'skill': 'PS4'}
view["age"] = 36 

print(allItems) # dict_items([('name', 'Walid'), ('skill', 'PS4'), 
# ('age', 36)])

print('=' *45)

# fromkeys()

a = ('myKey1', 'myKey2', 'myKey3')
b = "X"

print(dict.fromkeys(a, b)) # {'myKey1': 'X', 'myKey2': 'X', 'myKey3': 'X'}


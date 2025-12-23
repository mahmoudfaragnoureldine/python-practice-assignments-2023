# ----------------
# -- Dictionary --
# ----------------
# [1] Dict Items are Enclosed in curly braces
# [2] Dict Items are contains key : value
# [3] Dict key need to be immutable => (number, string, tuple) list not allowed
# [4] Dict value can have any data types
# [5] Dict key need to be unique
# [6] Dict is not orderd you access its element with key
# -----------------------

# Dictionary

user = {
    "name" : "Walid",
    "age" : 22,
    "country" : "Egypt",
    "skills" : ["Html", "Css", "Js"],
    "rating" : 10.5

}

print(user)
print(user['country'])     # Egypt
print(user.get('country')) # Egypt

print(user.keys())   # dict_keys(['name', 'age', 'country', 'skills', 'rating'])
print(user.values()) # dict_keys(['name', 'age', 'country', 'skills', 'rating'])

print("=" * 45)

# Two-Dimentional Dictionary

languages = {
    "one" : {
        "name": "Html",
        "progress": "80%"
    },
    "two" : {
        "name": "Css",
        "progress": "90%"
    },
    "three" : {
        "name": "Js",
        "progress": "90%"
    }
}

print(languages)
print(languages["one"]) # {'name': 'Html', 'progress': '80%'}
print(languages["three"]['name']) # Js

# Dictionary Length

print(len(languages)) # 3
print(len(languages["two"])) # 2

# Create dictionary from Variables

framework1 = {
    "name": "cpp",
    "progress": "80%"
}

framework2 = {
    "name": "c",
    "progress": "80%"
}

framework3 = {
    "name": "p",
    "progress": "80%"
}

allFrameWorks = {
    "one" : framework1,
    "two" : framework2,
    "three" : framework3
}

print(allFrameWorks)





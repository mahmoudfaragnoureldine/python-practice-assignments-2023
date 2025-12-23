# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------

# peoples = ["Walid", "Ahmed", "Sayed", "Ali"]

# skills = ["Html", "Css", "Js"]

# for name in peoples:  # Outer Loop
#    print(f"{name} Skills is: ")

#    for skill in skills:  # Inner Loop
#        print(f"- {skill}")


peoples = {
    "Walid": {"Html": "70%", "Css": "80%", "Js": "70%"},
    "Ahmed": {"Html": "90%", "Css": "80%", "Js": "90%"},
    "Sayed": {"Html": "70%", "Css": "60%", "Js": "90%"},
}

for name in peoples:
    print(f"Skills and Progress for {name} Is: ")

    for skill in peoples[name]:  # peoples[name] = peoples.get(name) = skills
        print(f"{skill} => {peoples[name][skill]}")

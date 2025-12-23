# -----------------------------------------------------
# -- Function Packing, Unpacking Arguments Trainings --
# -----------------------------------------------------

myTuble = ("Html", "Css", "Js")

mySkills = {"Go": "80%", "Python": "50%", "mySQL": "80%"}


def show_skills(name, *skills, **skillsWithProgress):
    print(f"Hello {name} \nYour skills without progress is: ")
    for skill in skills:
        print(f"- {skill}")

    print("Your skills with progress :")
    for skill_key, skill_value in skillsWithProgress.items():
        print(f"- {skill_key} => {skill_value}")


show_skills("Walid", *myTuble, **mySkills)

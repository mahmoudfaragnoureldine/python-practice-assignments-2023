# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------


# def show_skills(*skills):
#    print(type(skills))  # <class 'tuple'>
#    print("your skills is:")
#    for skill in skills:
#        print(skill)


# show_skills("C", "v", "c")

# ** بيبقي عايز منك تكتب ديكشنرى


def show_skills(**skills):
    print(type(skills))  # <class 'dict'>
    print("your skills is:")
    for key, value in skills.items():
        print(f"{key} => {value}")


show_skills(Html="80%", Css="70%", Js="50%")

class_name = "Introduction to Python"
intro = f"""
Welcome to the Python School Administration System!
---------------------------------------------------
Page: Roster
Class: {class_name}
"""

menu = """
Menu:
[1] Add student(s)
[2] Remove a student
[3] Remove all students
[4] List students
[5] Quit
"""

print(intro)
print(menu)

user_choice = None

while(user_choice != 4):
    user_choice = int(input("What would you like to do?"))

    match(user_choice):
        # todo: menu item 1
        # todo: menu item 2
        # todo: menu item 3
        # todo: menu item 4
        # todo: menu item 5
        case _:
            print("Invalid option!")
            print(menu)
# 3. Lists

list_of_misfits = list()


def validate_second_menu_input(question: str):
    user_input = input(question)
    if user_input.isdigit():
        return int(user_input)
    else:
        print("That's not an option my dude, please try again :)")


def add_misfit():
    while True:
        selected_action = validate_second_menu_input('Enter (1) to add a misfit or (2) to go back to the menu: ')
        if selected_action == 1:
            while True:
                name = input("What is the name of the misfit you'd like to add? ")
                if name in list_of_misfits:
                    print('misfit is already enrolled in this class. Please add another misfit.')
                else:
                    list_of_misfits.append(name)
                    print(f'{name} successfully enrolled to class!')
                    break
        else:
            menu()


def remove_misfit():
    if list_of_misfits:
        while True:
            selected_action = validate_second_menu_input('Enter (1) to remove a misfit or (2) to go back to the menu: ')
            if selected_action == 1:
                name = input("What is the name of the unfortunate misfit you'd like to remove? ")
                if name in list_of_misfits:
                    list_of_misfits.remove(name)
                    print(f'{name} successfully removed from class!')
                    break
                else:
                    print('misfit is not enrolled in class')
            else:
                menu()
    else:
        print('There are no misfits to remove :(')


def list_misfits():
    if list_of_misfits:
        print(", ".join(list_of_misfits))
    else:
        print('There are no misfits enrolled in this class.')


def options(selected_option: int):
    if selected_option == 1:
        add_misfit()
    elif selected_option == 2:
        remove_misfit()
    elif selected_option == 3:
        list_misfits()
    elif selected_option == 4:
        print('Exiting...')
        exit()


def validate_input(user_input: str):
    if user_input.isdigit():
        selected_option = int(user_input)
        if 1 <= selected_option <= 4:
            options(selected_option)
        else:
            print('Please only provide the number based on the options provided.')
    else:
        print("That's not an option my dude, please try again :)")


def menu():
    while True:
        print('Please select an option:')
        validate_input(
            input('Enter (1) Add a misfit (2) Remove a misfit in complete remission (3) List all misfits (4) Exit\n')
        )


print('This is the 2019 class of misfits! Whose life shall we ruin today?')
menu()

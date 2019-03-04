# 1. Character input exercise


# Method to check to user is providing a positive number only for number related inputs.
def number_input_for(question, error_message):

    while True:
        answer = input(question)
        if answer.isdigit():
            return answer
        else:
            print(error_message)


name = input('What is your name? ')

age_question = 'How old are you? '
age_error_message = "Please enter a number. Number must also be more than 0 because babies can't type."
age = number_input_for(question=age_question, error_message=age_error_message)

current_year_question = 'What year is it now? '
current_year_error_message = "Don't be silly, the current year must be positive, like me!"
current_year = number_input_for(question=current_year_question, error_message=current_year_error_message)
age_year_2050 = 2050 - int(current_year) + int(age)


country = input('Which country are you from? ')

print('Hi, ' + name + "! You're " + age + " years old and are from " + country + ". Cool!")
print("That means in 2050 you'll be " + str(age_year_2050) + " years old.")

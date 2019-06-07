# 2. Odd or even and divisors exercise

print(
    "Hello there! I am the magic number machine."
    "You can give me any positive number and I tell you interesting facts about them."
)
print("Let's begin!")


def validate_input_number(question: str):
    while True:
        user_input = input(question)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("That's not a number my dude. Please try again :)")


def odd_or_even(selected_number: int):
    if selected_number % 2 == 0:
        return 'even'
    else:
        return 'odd'


def get_divisors(selected_number: int):
    divisors = range(2, 11)
    value_is_a_multiple_of = list()
    for divisor in divisors:
        if selected_number % divisor == 0:
            value_is_a_multiple_of.append(str(divisor))

    if value_is_a_multiple_of:
        return "a multiple of " + ", ".join(value_is_a_multiple_of)
    else:
        return 'not a multiple of any number between 2 to 10'


selected_number = validate_input_number(question='What number did you have in mind? ')
print('Excellent number choice my dude!')
print('I have some interesting facts for you:')
print(f'- {selected_number} is an {odd_or_even(selected_number)} number')
print(f'- it is also a {get_divisors(selected_number)}')
print('Ta-dah! Magikk *popping noises*')

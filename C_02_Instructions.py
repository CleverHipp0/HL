def statement_generator(decoration, decoration_time, statement):
    """Makes a statement fancy by adding decorative characters"""

    print(f"\n{decoration * decoration_time} {statement} {decoration * decoration_time}\n")


def string_checker(question, valid_ans=("yes", "no")):
    """A simple string checker that defaults to 'yes' and 'no'."""

    error = f"This is not a valid input, please enter a valid answer from the list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:
            # check if the users response is in the word list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        print(error)


# Asks it the user wants instructions
want_instructions = string_checker("Do you want to see the instructions? ")

# Prints the instructions if that is what the user wants
if want_instructions == "yes":
    statement_generator("🧾", 3, "Instructions")
    print('''1. Pick a range that the number you will guess is in.
2. Start guessing numbers. Be careful though, you have limited guesses!
    ''')


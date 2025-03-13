# Check that users have entered a valid
# option based on a list
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


# Main routine goes here
answer_list = []

want_instructions = string_checker("Do you want instructions? ")

print(f"You choose:  {want_instructions}\n")

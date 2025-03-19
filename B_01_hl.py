import random
import math


def statement_generator(decoration, decoration_time, statement):
    """Makes a statement fancy by adding decorative characters"""

    print(f"\n{decoration * decoration_time} {statement} {decoration * decoration_time}\n")


def string_checker(question, valid_ans=("yes", "no")):
    """A simple string checker that defaults to 'yes' and 'no'."""

    error = f"This is not a valid input, please enter a valid answer from the list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for i in valid_ans:
            # check if the users response is in the word list
            if i == user_response:
                return i

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == i[0]:
                return i

        print(error)


def int_check(question, low=1, high=None, exit_code=None):
    """Checks for a number more than 0, accepts <enter> for infinite"""

    # Sets up an error message
    if exit_code != "xxx" and exit_code is not None:
        error = f"Please enter an whole number equal to or greater than {low} or <enter>."

    elif high is not None:
        error = f"Please enter an whole number between {low} and {high}."

    else:
        error = f"Please enter an whole number equal to or greater than {low}."

    while True:

        # Asks the question
        answer = input(question)

        # Returns if they input the exit code
        if answer == exit_code:
            return answer

        # Checks to see if they entered an integer
        try:
            answer = int(answer)

            if low > answer:
                print(error)

            elif high is not None and answer > high:
                print(error)

            else:
                return answer

        # if an integer was not inputted it will print the error
        except ValueError:

            print(error)


def cal_guesses(low, high):
    """Calculates the number of guesses"""
    number_range = high - low + 1
    max_raw = math.log2(number_range)
    max_upped = math.ceil(max_raw)
    maximum_guesses = max_upped + 1
    return maximum_guesses


def no_duplicates(low, high, guessed_list):

    while True:

        raw_number = int_check("Your guess: ", low, high, "xxx")

        if raw_number not in guessed_list:
            return raw_number

        print("You already guessed this number, try again")


def compare(num_1, num_2):

    if num_1 > num_2:
        print("Lower...")

    elif num_1 < num_2:
        print("Higher...")

    else:
        return "yes"


# Main routine goes here
print("🔼🔽🔼 Higher or Lower Game 🔼🔽🔼")

end_game = "no"
mode = "regular"
history = []


# Asks it the user wants instructions
want_instructions = string_checker("Do you want to see the instructions? ")

# Prints the instructions if that is what the user wants
if want_instructions == "yes":
    statement_generator("🧾", 3, "Instructions")
    print('''1. Pick a range that the number you will guess is in.
2. Start guessing numbers. Be careful though, you have limited guesses!
    ''')

# Asks how many game rounds
game_rounds = int_check("How many rounds do you want to play (press <enter> for infinite)? ", 1, exit_code="")


print()
lowest = int_check("Choose the lowest possible number: ", 1)
highest = int_check("Choose the highest possible number: ", lowest + 1)


if game_rounds == "":
    mode = "infinite"
    statement_generator("♾️", 3, "Infinite Mode")

else:
    statement_generator("📀", 3, f"Playing {game_rounds} rounds")

# loops until "xxx" is entered if the game mode is set to infinite
rounds_played = 0

while end_game == "no":

    # Round counter
    rounds_played += 1

    # Guessed numbers this round
    guessed = []

    # Sets the results to nothing
    results = ""

    # Nice heading
    statement_generator("🔃", 3, f"Round: {rounds_played}")

    # Randomise the secret number
    secret_number = random.randint(lowest, highest)

    # For testing
    print(secret_number)

    max_guesses = cal_guesses(lowest, highest)

    for item in range(0, max_guesses):

        if results != "":
            history.append(results)
            break

        print(f"\nGuess {item + 1}")

        choice = no_duplicates(lowest, highest, guessed)
        guessed.append(choice)

        if choice == "xxx":
            end_game = "yes"
            results = choice
            break

        final_choice = compare(choice, secret_number)

        if final_choice == "yes" and item == 0:
            results = "🍀 You guessed it first try!!! 🍀"

        elif final_choice == "yes":
            results = f"🎖️ You guessed it in {item + 1} tries!!! 🎖️"

        else:
            pass

    if results == "":
        results = "🥲 Nice try but you ran out of guesses! 🥲"
        history.append(results)

    print(f"{results}\n")

    if mode != "infinite" and rounds_played == game_rounds:
        end_game = "yes"

want_history = string_checker("Do you want to see your history? ")

if want_history == "yes":

    statement_generator("🛞", 3, "History")

    for number, item in enumerate(history):
        print(f"Round: {number + 1}")
        print(item)


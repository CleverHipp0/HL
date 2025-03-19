while True:

    choice_a = input("Number A: ")
    choice_b = input("Number B: ")

    if choice_a == "xxx" or choice_b == "xxx":
        print("Look the first if")
        break

    elif choice_a > choice_b:
        print("Lower...")

    elif choice_a < choice_b:
        print("Higher...")

    else:
        print("I got to the else statement!")



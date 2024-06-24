print("Your username will need at least 8 characters.")
username = input("Please enter a valid username: ")


def validator():
    if len(username) < 8:
        print("I'm sorry, your username is not long enough.\nPlease enter an 8 character username to continue.")
    else:
        print("Thank you for creating a username! Please proceed to creating a password.")

validator()
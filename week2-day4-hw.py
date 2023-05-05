# Exercises
# 1. Create a program that allows a user to continue to add people to an address book until the user quits. Once the user quits, break out of the loop and print out the name and address of everyone in the address book
# Steps
# Create a function that will ask user for name and addresses and stores them in a dictionary
# Define an empty dictionary with which to work (global or local variable?)
# Begin a loop that will continue to ask a user for information until the user "quits"
# If the user does not quit, ask for a name and address and store the values into variables
# Add information to the dictionary with name as the key and address as the value
# If the user does quit, end the loop
# Print out the information from the dictionary in a formatted way
# Execute/Call the function
# from IPython.display import clear_output
# while (ask := input('Enter something')) != 'quit':
# print(f"You entered: {ask}")
# if ask == 'clear':
# clear_output()
# Enter somethingquit

from IPython.display import clear_output
address_book = {}
you_got_this = True

while you_got_this:
    name = input("Enter your name: (or quit/clear)")

    num = input("Enter your number:  ")

    if name == "quit" or num == "quit":
        you_got_this = False
    if name == "clear" or num == "clear":
        clear_output()
        you_got_this = False
    address_book[name.title()] = num
    print(f'You\'ve added \', {address_book}')


# 2. Best Time to Meet
# Billy is trying to figure out if there is a time that he and his team can meet to work on the project. His three teammates each give him a list of times they are available ('HH:MM' 24-hour). Create a function that will take in an original list plus any number of lists of teammate's available times (*remember *args*) and return a list of times where everyone can meet.

ohh_billy = ["08:00", "09:09"]
billys_buddy1 = ["08:00", "09:15"]
billys_buddy2 = ["08:00", "09:12"]
billys_buddy3 = ["08:00", "09:02"]

# key value, name and time
times_that_match = {}


my_first_time = 0


def on_call(who_can_work):
    for w in who_can_work:
        times_that_match = times_that_match[my_first_time, w]
        my_first_time += my_first_time
    print(times_that_match)


on_call(ohh_billy)
on_call(billys_buddy1)
on_call(billys_buddy2)
on_call(billys_buddy3)

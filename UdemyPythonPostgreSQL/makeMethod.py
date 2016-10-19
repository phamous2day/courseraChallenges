import random

def ask_user_and_check_number():
    user_number=int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        print("You got the number correct!!")
    if user_number not in magic_numbers:
        print("You totally got the number WRONG!")

magic_numbers = [random.randint(0,9), random.randint(0,9)]



def run_program_x_times(chances):
    for attempt in range(chances): #range(changes) is [0,1,2]
        print("This is attempt{}".format(attempt))
        ask_user_and_check_number()

user_attempts = int(input("Enter number of attempts:  "))
run_program_x_times(user_attempts)

import random
def get_player_numbers():
    number_csv = input("Enter your 6 numbers, separated by commas: ")
    integer_set = {int(number) for number in number_list}
    return integer_set

def create_lottery_numbers():
    values = set()
    while len(values)<6:
        values.add(random.randint(1,20))
    return values
print(create_lottery_numbers())

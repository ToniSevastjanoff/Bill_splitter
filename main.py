import random

print("Enter the number of friends joining (including you):")
num_guests = int(input())
dict_guests = {}

if num_guests < 1:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for x in range(num_guests):
        guest = input()
        dict_guests[guest] = 0

    print("Enter the total bill value:")
    total = float(input())
    per_guest = round(total / num_guests, 2)

    for k, v in dict_guests.items():
        dict_guests[k] = per_guest

    answer = ""
    while answer != "Yes" and answer != "No":
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        answer = input()

    if answer == "Yes":
        random.seed()
        lucky_one = random.randrange(1, num_guests)
        print(list(dict_guests)[lucky_one] + " is the lucky one!")
        lucky_name = list(dict_guests)[lucky_one]

        new_per_guest = round(total / (num_guests - 1), 2)

        for k, v in dict_guests.items():
            dict_guests[k] = new_per_guest

        dict_guests[lucky_name] = 0

        print(dict_guests)

    else:
        print("No one is going to be lucky")
        print(dict_guests)
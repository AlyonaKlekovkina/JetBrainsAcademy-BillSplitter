import random


def get_number_of_people():
    while True:
        number = input("Enter the number of friends joining (including you):\n")
        try:
            if int(number) <= 0:
                return "No one is joining for the party"
            else:
                return number
        except ValueError:
            return "No one is joining for the party"


def create_dict():
    global number_of_people
    list_of_people = {}
    n = number_of_people
    print("Enter the name of every friend (including you), each on a new line:")
    while n > 0:
        inp = input()
        list_of_people.update({inp: 0})
        n -= 1
    total_bill = int(input('Enter the total bill value:\n'))
    split_value = round(total_bill/number_of_people, 2)
    l = len(list_of_people)
    while l > 0:
        for v in list_of_people:
            list_of_people.update({v: split_value})
            l -= 1
    return list_of_people


def who_is_lucky():
    global the_list
    get_answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if get_answer == 'Yes':
        r = random.choice(list(the_list.keys()))
        print(r, 'is the lucky one!')
    else:
        print('No one is going to be lucky')


number_of_people = get_number_of_people()
if number_of_people == "No one is joining for the party":
    print("No one is joining for the party")
else:
    number_of_people = int(number_of_people)
    the_list = create_dict()
    who_is_lucky()


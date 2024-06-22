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
    print("Enter the name of every friend (including you), each on a new line:")
    while number_of_people > 0:
        inp = input()
        list_of_people.update({inp: 0})
        number_of_people -= 1
    return list_of_people


number_of_people = get_number_of_people()
if number_of_people == "No one is joining for the party":
    print("No one is joining for the party")
else:
    number_of_people = int(number_of_people)
    the_list = create_dict()
    print(the_list)

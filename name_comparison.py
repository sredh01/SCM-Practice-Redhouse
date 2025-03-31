import pandas as pd

honors_user_name = []
list_user_name = []
stuff = []
JNumber =[]


def process_user_honors_names(input_file):
    data = pd.read_csv(input_file)

    fullname = data['First Name'] + ' ' + data['Last Name']

    for name in fullname:
        honors_user_name.append(name)


def process_user_list_names(list_file_names):
    data = pd.read_csv(list_file_names)
    list_of_names = data['Last Name'] + ' ' + data['First Name']

    for name in list_of_names:
        list_user_name.append(name)

def compare(list1, list2):
    exists = []
    DNE = []

    if list1 == list2:
        return True
    else:
        for names in list1:
            if names in list1:
                exists.append(names)
            else:
                DNE.append(names)

        for name in list2:
            if name not in list1:
                DNE.append(name)

    return exists, DNE


input_file = ''

list_file_names = ''
process_user_honors_names(input_file)

process_user_list_names(list_file_names)

alive, not_alive = compare(honors_user_name, list_user_name)

# This probably not accurate not sure. Just coded it quickly. Does not show user name corresponding External ID.
print("The list of names that are in the list: ")
for name in alive:
    print(name)

print("\nThe list of names that are not in the list: ")
for names in not_alive:
    print(names)

import pandas as pd

honors_user_name = []
list_user_name = []
stuff = []


def process_user_honors_names(input_file):
    data = pd.read_csv(input_file)

    fullname = (data['First Name'] + ' ' + data['Last Name']).str.strip().str.lower()

    for name in fullname:
        honors_user_name.append(name)


def process_user_list_names(list_file_names):
    data = pd.read_csv(list_file_names)
    list_of_names = (data['Last Name'] + ' ' + data['First Name']).str.strip().str.lower()

    for name in list_of_names:
        list_user_name.append(name)


def compare(list1, list2):
    exists = []
    DNE = []

    for names in list1:
        if names in list2:
            exists.append(names)
        else:
            DNE.append(names)

    for names in list2:
        if names not in list1:
            DNE.append(names)

    return exists, DNE


input_file = ''  # Insert file path
list_file_names = ''  # Insert file path

process_user_honors_names(input_file)

alive, not_alive = compare(honors_user_name, list_user_name)

# This probably not accurate not sure. Just coded it quickly. Does not show user name corresponding External ID.
print("The list of names that are in the list: ")
for name in alive:
    print(name)

print("\nThe list of names that are not in the list: ")
for names in not_alive:
    print(names)

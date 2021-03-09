f = open("D:\Projects\AdventOfCode\Day4\InputData.txt", "r")
data = f.read()

input_data = data.split('\n\n')

formatted_data = [entry.replace('\n',' ').split(' ') for entry in input_data]
list_data = []
dict_data = []

for entry in formatted_data:
    list_data = list_data +  [[element.split(':') for element in entry]]

for entry in list_data:
    dict_data = dict_data + [dict(entry)]

all_keys_in_dict = list(set([item for sublist in [[*i] for i in dict_data] for item in sublist]))

def check_birth_year(entry):
    if not(len(entry) == 4):
        return False
    elif not(int(entry) >= 1920 and int(entry) <= 2002):
        return False
    else:
        return True

def check_issue_year(entry):
    if not(len(entry) == 4):
        return False
    elif not(int(entry) >= 2010 and int(entry) <= 2020):
        return False
    else:
        return True

def check_expiration_year(entry):
    if not(len(entry) == 4):
        return False
    elif not(int(entry) >= 2020 and int(entry) <= 2030):
        return False
    else:
        return True

def check_height(entry):
    if entry[-2:] == 'cm':
        if not(int(entry[:-2]) >= 150 and int(entry[:-2]) <= 193):
            return False
        else:
            return True
    elif entry[-2:] == 'in':
        if not(int(entry[:-2]) >= 59 and int(entry[:-2]) <= 76):
            return False
        else:
            return True
    else:
        return False


def check_hair_color(entry):
    alphabet = list('abcdef')
    number = list('0123456789')
    if not(len(entry) == 7):
        return False
    elif not(entry[0] == '#'):
        return False
    elif not(set(list(entry[1:])) <= set(alphabet).union(set(number))):
        return False
    else:
        return True

def check_eye_color(entry):
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if not(len(entry) == 3):
        return False
    elif not(set([entry]) <= set(valid_colors)):
        return False
    else:
        return True

def check_passport_id(entry):
    valid_numbers = list('0123456789')
    if not(len(entry) == 9):
        return False
    elif not(set(entry) <= set(valid_numbers)):
        return False
    else:
        return True

invalid = 0
valid = 0
invalid_item_list = []
for index, entry in enumerate(dict_data):
    for item in all_keys_in_dict:
        # Loose rules
        if item not in [*entry]:
            if item != 'cid':
                invalid_item_list.append(item)
        else:
            # Strict Rules
            if item == 'byr':
                if check_birth_year(entry[item]) is False:
                    invalid_item_list.append(item)
            if item == 'iyr':
                if check_issue_year(entry[item]) is False:
                    invalid_item_list.append(item)
            if item == 'eyr':
                if check_expiration_year(entry[item]) is False:
                    invalid_item_list.append(item)
            if item == 'hgt':
                if check_height(entry[item]) is False:
                    invalid_item_list.append(item)
            if item == 'hcl':
                if check_hair_color(entry[item]) is False:
                    invalid_item_list.append(item)
            if item == 'ecl':
                if check_eye_color(entry[item]) is False:
                    invalid_item_list.append(item)
            if item == 'pid':
                if check_passport_id(entry[item]) is False:
                    invalid_item_list.append(item)

    if len(invalid_item_list) >= 1:
        invalid += 1
        print('Index : {0:<5} Invalid : {1:50} Count : {2}'.format(index, str(invalid_item_list), invalid))
    invalid_item_list.clear()


print('\nNumber of valid passports : {0}'.format(len(dict_data) - invalid))
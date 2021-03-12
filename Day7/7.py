import re

f = open("./TestData.txt", "r")
raw_data = f.read()

list_data = raw_data.split('\n')
processed_data = []

for entry in list_data:
    pass_1 = re.sub("(contain)|(bags+)|(\,+)|(\.+)|(no\s+other)", " ", entry)
    pass_2 = re.sub("(\s{2,})|([ \t]+$)",",",pass_1)
    # pass_3 = pass_2.rsplit(',', 1)[0] # Tried to use regex, split my head, went back to rsplit.
    pass_3 = re.sub(",(?!.*,)", "",pass_2) # Tried to use regex, split my head, went back to rsplit.
    print("{0}\n".format(pass_3))
    processed_data.append(pass_3.split(','))
# regex : /(\s+contain\s+)|(bags*)|(,)|(\s+)|(\.+)|(no\sother)/gm
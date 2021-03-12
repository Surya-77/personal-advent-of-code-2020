import re

txt = "light red bags contain 1 bright white bag, 2 muted yellow bags."
pass_1 = re.sub("(contain)|(bags+)|(\,+)|(\.+)", " ", txt)
pass_2 = re.sub("(\s{2,})|([ \t]+$)",",",pass_1)
pass_3 = pass_2.rsplit(',', 1)[0] # Tried to use regex, split my head, went back to rsplit.
print(pass_1)
print(pass_2)
print(pass_3)
import re

min_length = 5  # Specify the minimum length here
max_length = 10  # Specify the maximum length here

pattern = r"^iCapital.{" + str(min_length) + r"," + str(max_length) + r"}Fund$"

string1 = "iCapitalHelloWorldFund"
string2 = "iCapitalPythonIsGreatFund"
string3 = "iCapitalShortFund"

if re.match(pattern, string1):
    print("String 1 matches the pattern.")
else:
    print("String 1 does not match the pattern.")

if re.match(pattern, string2):
    print("String 2 matches the pattern.")
else:
    print("String 2 does not match the pattern.")

if re.match(pattern, string3):
    print("String 3 matches the pattern.")
else:
    print("String 3 does not match the pattern.")

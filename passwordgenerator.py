import random



lower_char = ['a', 'b', 'c', 'd', 'e']
upper_char = ['A', 'b', 'C', 'D', 'E']
numeric_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['@', '#', '$', '%', '*']
password = random.choice(lower_char) + random.choice(upper_char) + random.choice(numeric_char) + random.choice(special_char)
password = password + password

print(password)

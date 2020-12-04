lines = []
valid_passwords = 0

#read and parse lines
with open('Day2PuzzleInputs.txt', 'r') as file:
    lines = file.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].replace('-', " ")
        lines[i] = lines[i].replace(':', '')
        lines[i] = lines[i].split(' ')
        lines[i][3] = lines[i][3].replace('\n', '')

#Calculte if passwords are valid and count the number of valid passwords.

for line in lines:
    target_letter = line[2]
    lower_bound = int(line[0])
    upper_bound = int(line[1])
    if line[3].count(target_letter) >= lower_bound and line[3].count(target_letter) <= upper_bound:
        print(f"{line[3]} is a valid password!")
        valid_passwords += 1
    else:
        print(f"{line[3]} is not a valid password!")


#print number of valid passwords
print(f"Number of valid passwords: {valid_passwords}")
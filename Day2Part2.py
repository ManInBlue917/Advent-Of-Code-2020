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
    letters_at_index = 0
    target_letter = line[2]
    lower_index = int(line[0]) - 1
    upper_index = int(line[1]) - 1

    if line[3][lower_index] == target_letter:
        letters_at_index += 1
    if line[3][upper_index] == target_letter:
        letters_at_index += 1
    
    if letters_at_index == 1:
        valid_passwords += 1


#print number of valid passwords
print(valid_passwords)
h_pos = 0
trees_hit = 0

with open('Day3PuzzleInputs.txt', 'r') as file:
    lines = file.readlines()

    for line in lines:
        if line[h_pos % 31] == '#':
            trees_hit += 1
            print("Tree Hit")
        else:
            print("Tree Missed")
        h_pos += 3
        
    print(f"Number of trees hit: {trees_hit}")
h_pos = 0
trees_hit = 0
index = 0

answers = []
multiplied_answer = 1

angles = [[1, 1], 
          [3, 1], 
          [5, 1], 
          [7, 1], 
          [1, 2]]

with open('Day3PuzzleInputs.txt', 'r') as file:
    lines = file.readlines()

    for angle in angles:
        index = 0
        h_pos = 0
        trees_hit = 0
        while index < len(lines):
            if lines[index][h_pos % 31] == '#':
                trees_hit += 1
                print("Tree Hit")
            else:
                print("Tree Missed")
            h_pos += angle[0]
            index += angle[1]
        
        answers.append(trees_hit)
    
    print(answers)

    for answer in answers:
        multiplied_answer = multiplied_answer * answer
    
    print(multiplied_answer)
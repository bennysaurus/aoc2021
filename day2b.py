file1 = open('day2.input.txt', 'r')
Lines = file1.readlines()

depth = 0
horizontal = 0
aim = 0;
 
for line in Lines:
    instruction = line.split()
    if instruction[0] == 'forward': 
        horizontal += int(instruction[1])
        depth += (int(instruction[1])*aim)
    if instruction[0] == "down": aim += int(instruction[1])
    if instruction[0] == "up": aim -= int(instruction[1])
        
print("Depth: " + str(depth))
print("Horizontal: " + str(horizontal))
print(depth*horizontal)
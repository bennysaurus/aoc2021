file1 = open('day1a.input.txt', 'r')
Lines = file1.readlines()
 
count = 0
previous = 99999

for line in Lines:
    if previous < int(line):
        count += 1
    previous = int(line)
print(count)
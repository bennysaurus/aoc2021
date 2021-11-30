# Read file, grab 4 values and do the compare.
# If lesser, add to total. Break if run out of numbers,
# seek back 3 spots to start the process again.
total = 0
count1 = 0
count2 = 0

with open('day1a.input.txt', 'r') as fp:
    while True:
        try :
            int1 = int(fp.readline())
            last_pos = fp.tell()
            int2 = int(fp.readline())
            int3 = int(fp.readline())
            int4 = int(fp.readline())
        except ValueError:
            break
        count1 = int1 + int2 + int3
        count2 = int2 + int3 + int4
        if count1 < count2: total += 1

        fp.seek(last_pos)

print(total)

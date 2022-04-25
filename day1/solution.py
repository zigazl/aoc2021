
input = open("input.txt", "r+")
lines = input.readlines()
count = 0
# part1
for i in range(len(lines)-1):
    if int(lines[i+1]) > int(lines[i]):
        count += 1

# part2
count = 0
for i in range(len(lines)-3):
    if int(lines[i+1]) + int(lines[i+2])+int(lines[i+3]) > int(lines[i]) + int(lines[i+1]) + int(lines[i+2]):
        count += 1


print("solution is "+str(count))

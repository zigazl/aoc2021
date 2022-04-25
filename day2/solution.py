input = open("input.txt", "r+")
lines = input.readlines()

horizontal = 0
depth = 0
aim = 0

for i in lines:
    step = str(i.split(" ")[0])
    value = int(i.split(" ")[1])
    if step == "forward":
        horizontal += value
        depth += aim * value
    if step == "up":
        #depth -= value
        aim -= value
    if step == "down":
        #depth += value
        aim += value


print("solution is depth:" + str(depth) + "horizontal:" + str(depth))
print(horizontal*depth)

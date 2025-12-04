dial = 50
step = 0


with open("day1.txt") as file:
    lines = file.readlines()


for i, line in enumerate(lines, start=1):
    print(dial)
    print(line)
    letter = line[0]
    print(letter)
    if letter == "R":
        for y in range(int(line[1:])):
            dial += 1
            if dial == 100:
                dial = 0
                step += 1
                print("wrapped around, step increased to ", step)
    elif letter == "L":
        for y in range(int(line[1:])):
            dial -= 1
            if dial == -1:
                dial = 99
                step += 1
                print("wrapped around, step increased to ", step)

    if dial == 0 and letter == "L":
        step += 1
        print("hit zero, step increased to ", step)

print(step)



#   print(f"{i}: {line}")

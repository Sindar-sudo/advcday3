with open("day3.txt") as file:
    lines = file.readlines()
total = 0


for line in lines:
    length = len(line.strip())
    maxnum = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    maxpoz = -1
    number = ""
    for k in range(12, 0, -1):
        maxinline = 0
        for i in range(length - k, maxpoz, -1):
            if int(line[i]) >= int(maxinline):
                maxinline = line[i]
                maxpoz = i
        maxnum[k] = maxinline
        #print(maxnum)
    print(maxnum)
    for j in range(12, 0, -1):
        number += str(maxnum[j])
        print(maxnum[j])
        print('next')
    print(number)
    total += int(number)
print(total)
    
"""    for i in range(length-2 ,-1,-1):
#        if int(line[i]) >= int(maxnum):
#            maxnum = line[i]
#            maxindex = i
#    for y in range(length -1,maxindex,-1):
#        if int(line[y]) >= int(maxnum2):
#            maxnum2 = line[y]
    maxstr = str(maxnum) + str(maxnum2)
    print(maxstr)
    total += int(maxstr)
    #print(total)

print(total)
"""

        
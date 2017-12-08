fp = open("input.txt","r")
strs = fp.readlines()
l = ["H","S","A","G","M"]

for i in range (26):
    print('%2d'%(i),end=" ")
for i in range (5):
    print()
    for line in strs:
        _exist=0
        for word in line:
            if word == l[i]:
                _exist = 1
        print("%2d" %(_exist),end=" ")

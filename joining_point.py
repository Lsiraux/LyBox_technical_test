import sys

# Body of the  ComputeJoinPoint function :

s1 = int(input("sequence 1 : "))
s2 = int(input("sequence 2 : "))
string1 = str(s1)
string2 = str(s2)
list1 = []
list2 = []
list1.append(s1)
list2.append(s2)

while s1 != s2:
    for i in range(len(string1)):
        s1 += int(string1[i])
    if s1 in list2:
        print(s1)
        exit(0)
    for i in range(len(string2)):
        s2 += int(string2[i])
    if s2 in list1:
        print(s2)
        exit(0)
    string1 = str(s1)
    string2 = str(s2)
    list1.append(s1)
    list2.append(s2)

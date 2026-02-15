n = int(input())
s = input()
letter = list(s)

danik = 0
anton = 0
for i in range(len(letter)):
    if letter[i] =="D":
        danik += 1
    elif letter[i] =="A":
        anton += 1
if danik > anton:
    print("Danik")
elif danik < anton:
    print("Anton")
else:
    print("Friendship")

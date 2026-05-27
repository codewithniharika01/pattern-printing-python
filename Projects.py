for i in range(5):
    print(" * * * * *")

for i in range(1,6):
    print("*" *i)

for i in range (5,0 ,-1):
    print("*" * i)

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end = " ")
    print()

for i in range(1,6):
    print((str(i) + " ") * i)

num = 1

for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

for i in range(65, 70):
    for j in range(65, i + 1):
        print(chr(j), end=" ")
    print()



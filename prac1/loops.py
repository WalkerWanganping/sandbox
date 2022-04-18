for i in range(1, 21, 2):
    print(i, end=' ')
print()


#a

for i in range(0, 101, 10):
    print(i, end=' ')
print()


#b

for i in range(20, 0, -1):
    print(i, end=' ')
print()


#c

star_number = int(input("enter number of stars:"))
for i in range(1, star_number+1):
    print("*", end='')
print()


#d

star_number = int(input("enter number of stars:"))
for i in range (1,star_number+1,1):
    for j in range(1,i+1):
        print("*", end='')
    print()

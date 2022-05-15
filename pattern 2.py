n = int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(63+i+1),end=" ")
    print()
n = int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(63+j+1),end=" ")
    print()
    
print("---------------------------")
n = int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(65+n-i),end=" ")
    print()

n = int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(65+n-j),end=" ")
    print()
print("--------------")
n = int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(96+j),end=" ")
    print()

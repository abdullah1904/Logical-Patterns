def pattern1(n):
    for i in range(n):
        for j in range(n):
            print('*',end=" ")
        print()

def pattern2(n):
    for i in range(n):
        for j in range(0,i+1):
            print('*',end=" ")
        print()

def pattern3(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

def pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end=" ")
        print()

def pattern5(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print('*', end=" ")
        print()

def pattern6(n):
    for i in range(n):
        for j in range(1,n+1-i):
            print(j, end=" ")
        print()

pattern6(5)
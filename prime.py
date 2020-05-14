def Prime(m,n):

    for i in range(m,n+1):
        f = False
        for j in range(2,i):
            if(i%j==0):
                f = True
                break

        if(f):
            continue
        else:
            print(i,end=" ")



m=int(input("Enter first number:"))
n=int(input("Enter second number:"))
if m > n:
    Prime(n,m)
if n > m:
    Prime(m,n)
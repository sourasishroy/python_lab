while True:
    A=int(input("Enter a non negetive number : "))
    if A<0 or A>1000:
        print("Invalid. Please try again.")
    else:
        break
         
a=0
b=0
c=1
lst=[]
print("The a,b pairs are as follows :")
for a in range (33):
    for b in range (33):
        if a <= b:
            if ((a*a)+(b*b) == A):
                print("(a",c,",","b",c,") = (",a,",",b,")")
                lst.append(a)
                c+=1
if len(lst) == 0 :
    print("Number doesn't satisfy Pythagoras Theorem")
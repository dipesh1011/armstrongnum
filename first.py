count=0
for n in range(100, 999):
#n=int(input('Enter any three digit numbr'))
    m=n
    c=int(n%10)
    n=int(n/10)
    b=int(n%10)
    n=int(n/10)
    a=int(n%10)
    n1=int(a*a*a+b*b*b+c*c*c)
    if m==n1:
        #print("It is a armstong number")
        print(n1)
        count=count+1
print(count)



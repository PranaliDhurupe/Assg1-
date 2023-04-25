#program to find fibonacci series

n = int(input("value for sequence: "))
n1=0
n2=1

if n<=0:
    print("Sequence:",n1)


else:
    print("sequence:")
    print(n1)
    print(n2)
    for x in range(2,n):
        term=n1+n2
        print(term)
        n1=n2
        n2=term

a = int(input("Enter a1: "))
b = int(input("Enter b1: "))
c = int(input("Enter a2: "))
d = int(input("Enter b2: "))


g = [a,b]
g.sort()


k = [c,d]
k.sort()

if g[-1] > k[-1]:
    i = g[-1]
    e = g[1]-g[0]
    if k[0] <= e:
        print("The side of the square is: ", i)
        print("The minimum area of square is:",i*i)
    else:
        i += k[0] - e
        print("The side of the square is: ", i)
        print("The minimum area of square is:",i*i)
else:
    i = k[-1]
    e = k[1]-k[0]
    if g[0] <= e:
        print("The side of the square is: ", i)
        print("The minimum area of square is:",i*i)
    else:
        i += g[0] - e
        print("The side of the square is: ", i)
        print("The minimum area of square is:",i*i)
        
        
        
        
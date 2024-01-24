def miyona (a,b,c):
    d= max(a,b,c)
    m= min(a,b,c)
    return((a+b+c)-(d+m))
    
a = int(input())
b = int(input())
c = int(input())
print(miyona(a,b,c))

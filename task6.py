a = int(input())
def summing(a):
   
    max = -9999 
    min = 9999
    s = 0
    i = a
    while i > 0:
        s = i % 10
        if s > max:
            max = i % 10
        elif s < min:
            min = i % 10  
            i//=10  
    print(max + min )
summing(a)
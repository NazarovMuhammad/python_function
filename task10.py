def neg_pos (a,b):
    if a%b==0:
      return("YES")
    else:
        return("NO")
    
a = int(input())    
b = int(input())
print(neg_pos(a,b))
def triangle(sides):
    i=sides-1
    c=1
    while i>=0:
        print(" "*i + " ".join("*"*c) )
        c+=1
        i-=1

def rtriangle(sides):
    i=0
    c=1
    while i<sides:
        print(" ".join("*"*c) )
        c+=1
        i+=1
    
triangle(8)
rtriangle(8)
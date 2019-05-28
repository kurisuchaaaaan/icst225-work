def triangle_perimeter (a, b, c):
    # < your code here >
    return (a + b + c)

def triangle_heronsarea (a, b, c):
    # < your code here >
    s = triangle_perimeter(a,b,c)/2
    sidea = s - a   
    sideb = s - b
    sidec = s - c 
    import math
    return math.sqrt(s * sidea * sideb * sidec)
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def is_right_triangle(a, b, c):
    return (a**2 + b**2 == c**2) or \
           (a**2 + c**2 == b**2) or \
           (b**2 + c**2 == a**2)

# Taking input
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if is_triangle(a, b, c):
    print("It is a valid triangle")
    
    if is_right_triangle(a, b, c):
        print("The triangle is Right-Angled")
    else:
        print("The triangle is NOT Right-Angled")
else:
    print("Not a valid triangle")

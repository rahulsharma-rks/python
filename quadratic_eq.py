import cmath
a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))
d = (b**2)-(4*a*c)
r1 = (-b - cmath.sqrt(d))/(2*a)
r2 = (-b + cmath.sqrt(d))/(2*a)
print("Solution:{0} and {1}".format(r1,r2))


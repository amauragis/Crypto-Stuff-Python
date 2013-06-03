import jacobi

n = 481
epps = list()
#for a in range(11,11):
a = 11
js = jacobi.jacobi(a,n)
print a**((n-1)/2)%n
print js %n
if (js%n != 0) and (a**((n-1)/2)%n == js %n):
    epps.append(a)

print epps

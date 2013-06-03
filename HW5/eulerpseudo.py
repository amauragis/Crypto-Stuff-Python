import jacobi

n = 69
epps = list()
for a in [3, 11, 22, 68]:
    js = jacobi.jacobi(a,n)
    if (js%n != 0) and (a**((n-1)/2)%n == js %n):
        epps.append(a)

print epps

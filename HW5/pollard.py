import fractions

def pollard(n, B):
    a = 2
    for j in range(2,B+1):
        print a
        a = a**j % n
    d = fractions.gcd(a-1, n)
    if (1 < d and d < n):
        return "Answer: " + str(d)
    else:
        return "nope"
if __name__ == '__main__':
    print pollard(4353,   20)
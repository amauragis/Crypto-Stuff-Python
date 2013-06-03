
def millerrabin(n, a):
    k = 0
    m = n - 1
    while ((m & 1) != 1):
        k += 1
        m = m >> 1
    
    b = a**m % n
    if b == (1 % n):
        return("n is prime 1")
    for i in range(k):
        print i
        if b == (-1 % n):
            return("n is prime 2")
        else:
            b = (b*b) % n
    return ("n is composite")
        
if __name__ == '__main__':
    print millerrabin(13313, 2)
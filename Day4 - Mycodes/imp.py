
def m(n):
    p = True
    #a = p for n in range(2, n) if n % q == 0 p is False
    #return a
    for q in range(2, n):
        if n % q == 0:
            p = False
        break
    return p

r = 19
s = m(r)
print(s)
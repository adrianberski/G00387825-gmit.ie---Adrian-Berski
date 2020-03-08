p = 347
m = 2
isprime = True

while m < p:
    if p % m == 0:
        isprime = False
        break
    m = m + 1

    if isprime:
        print (p, "is a prime number.")
    else:
        print (p, "is not prime.")






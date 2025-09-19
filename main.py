import math
import numpy as np

def isprime(p):
    ''' - prend en argument un nombre entier p

        - retourne un booléen exprimant la vérité de « p est un nombre premier ».

    >>> is_prime(5)
     5 :True 
    '''

    if p<2:
        return False
    for i in range(2, math.floor(np.sqrt(p))+1):
        if p%i==0:
            return False
    return True

def main():
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()


if __name__ == "__main__":
    main()
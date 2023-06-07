# extended Euclidean algorithm
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x
 
 
if __name__ == '__main__':

    m=int(input("Enter number1:")) #num whose mod to be found
    y=int(input("Enter number2")) #num whose inv to be found
    gcd, x, y = extended_gcd(m, y)
    if gcd!=1:
        print("Inverse doesn't exists")
    else:
        print('The inverse is', y%m)

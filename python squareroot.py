# A program that takes a positive floating-point number as input and outputs an 
# approximation of its square root.

#first Iam budling a fucntion sqrt with one parameter named number
def sqrt(number):
    #return number **(1/2) - I am using exponents (**) to return the square root of number.
    #Converting a number  into an string
    return "The square root of " +str(number) + " is approx. " + str(number **(1/2)) 

print(sqrt(14.5))





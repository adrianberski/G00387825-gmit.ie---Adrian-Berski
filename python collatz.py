#program that asks the user to input any positive integer 
# and outputs the successive values of 
# the following calculation. At each step calculate 
# the next value by taking the current value and,
#  if it is even, divide it by two, but if it is odd, 
# multiply it by three and add one. Have the program 
# end if the current value is one.

#STEP 1 
i = int(input("Please enter a positive integer: "))
# while I doesn`t not reach 1 (not equal)
while i != 1:
    print (i, end= ", ")
    #to determine if  integer is even or odd number (using modular)
    if (i % 2) ==0:
        i = i // 2
    else:
        i = i * 3 + 1
print (i)


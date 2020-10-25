# This programme calculates BMI
# test for git - A line of text preceded by a # is 
# called a comment. 

# defining variables
# using floats as I have numbers with a decimal point
# I can  can reassign variables

weight = float(input ("Please enter you weight in KG: " ))
height = float (input ("Please enter your height in CM: "))
# *100 as output is their weight divided by their height 
# in metres squared.
height = height/100 

output = weight / (height * height)



print ("Your BMI is", output )







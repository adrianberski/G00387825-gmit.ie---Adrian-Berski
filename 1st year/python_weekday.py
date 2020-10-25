# A program that outputs whether or not today is a weekday. 
#This is first version, inmature one: 

# i to define input, and ask end user to provide the specific day 
i = input("Please enter which day is today (from Monday to Sunday)?")
#here I am providing codtions if - This is the form of a conditional statement
if i == ("Monday"):
    #if conditions equals to - this operator compare two items and return True or False
     print("Yes, unfortunately today is a weekday")
     #elif=else if , an elif statement checks another condition after the 
     # previous if statements conditions aren’t met
elif i ==("Tuesday"):
     print("Yes, unfortunately today is a weekday")
elif i ==("Wednesday"):
     print("Yes, unfortunately today is a weekday")
elif i ==("Thursday"):
     print("Yes, unfortunately today is a weekday")
elif i ==("Friday"):
    print("Yes, unfortunately today is a weekday")
    # else  statements allow me to elegantly describe what I want my code to do 
    # when certain conditions are not me
else:
    print("It is the weekend, yay!")

# it can be function but I think that purpouse for this excercise was to use conditions and
#to control flow 

#mature version 
#i = input("Please enter which day is today (from Monday to Sunday)?")
#weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#if weekdays.include(i):
#	print("Yes, unfortunately today is a weekday")
#else:
#	print("It is the weekend, yay!")
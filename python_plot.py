#A program that displays a plot of the functions
#  f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

#Before I start working with task, I need to import it into my Python environment.
import matplotlib.pyplot as plt
import numpy as np


# Create functions and using data
x = [0, 1, 2, 3, 4]
f = [0, 1, 2, 3, 4]
g = [0, 1, 4, 9, 16]
h = [0, 1, 8, 27, 64]

#def g(a, b, c, d, e):
 #   f = a**2
  #  s = b**2
   # t = c**2
    #fo = d**2
    #fi = e**2
    #return f, s, t, fo, fi
#print (g(0, 1, 2, 3, 4))


#def h(a, b, c, d, e):
    #f = a**3
    #s = b**3
    #t = c**3
    #fo = d**3
    #fi = e**3
    #return f, s, t, fo, fi
#print (h(0, 1, 2, 3, 4))


#def h(x):
    #return (x) * 3



#create plots with above data
plt.plot (x, f)
plt.plot (x, g)
plt.plot (x, h)

#swow plots for 3 functions 
plt.show()



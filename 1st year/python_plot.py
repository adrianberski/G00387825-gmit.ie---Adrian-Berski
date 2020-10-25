#A program that displays a plot of the functions
#  f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

#Before I start working with task, I need to import it (particular libraries)
#  into my Python environment.
import matplotlib.pyplot as plt
import numpy as np


# Create functions and using data
#x = [0, 1, 2, 3, 4] or x = range(4)
#f = [0, 1, 2, 3, 4]
#g = [0, 1, 4, 9, 16] - from function gf
#h = [0, 1, 8, 27, 64] - from functiongf


def gf(a, b, c, d, e):
    f = a**2
    s = b**2
    t = c**2
    fo = d**2
    fi = e**2
    return f, s, t, fo, fi



def hf(a, b, c, d, e):
    f = a**3
    s = b**3
    t = c**3
    fo = d**3
    fi = e**3
    return f, s, t, fo, fi


x = [0, 1, 2, 3, 4]
f = [0, 1, 2, 3, 4]
g = gf(0, 1, 2, 3, 4)
h = hf(0, 1, 2, 3, 4)



#create plots with above data on the one set of axes
plt.plot (x, f)
plt.plot (x, g)
plt.plot (x, h)

#swow plots for 3 functions on the one set of axes
plt.show()




#A programe that outputs a summary of each variable (from the Iris data set) to a 
# single text file,saves a histogram of each variable to png files, and
# outputs a scatter plot of each pair of variables.

#Before I start working with task, I need to import it (particular libraries)
# into my Python environment. My programe requires Prerequisites Python libraries such as: 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import seaborn as sns
import statistics as st
import csv

#This applies to all parts
# this will read a comma-separated values (csv) file into DataFrame.
#Read a comma-separated values (csv) file into DataFrame. In my case the iris.csv.
df = pd.read_csv("iris.csv")

print(df.info())

print(df.describe())
#This method prints information about a DataFrame including the index dtype and column dtypes, 
# non-null values and memory usage. = summary of each variable
#2nd descriptive statistics method includes those that summarize the central tendency,
#  dispersion and shape of a dataset’s distribution, excluding NaN values.
#Part1
f = open('summary of each variable.txt', 'w+')
df.info(buf=f) 
f.close()
#above I am saving output from df into a txt. file 'summary of each variable.txt'

#Part2
#plt. figure() is to create a figure object. The whole figure is regarded as the figure object.
#I specified the figure size below and it takes t takes a tuple of two values, the width and height of the 
# figure in cm. 
plt.figure(figsize = (10, 7)) 
x = df["sepal_width"] 
plt.hist(x, bins = 20, color = "green") 
plt.title("Sepal Width in cm") 
plt.xlabel("Sepal_width_cm") 
plt.ylabel("Count")
plt.show()
#plt. show() starts an event loop, looks for all currently active figure objects, and opens one or more interactive
#  windows that display your figure or figures. The plt. show() command does a lot under the hood, 
# as it must interact with your my interactive graphical backend - more info at readme file.

#below is the same for fifferent variable
plt.figure(figsize = (10, 7)) 
x = df["sepal_length"] 
plt.hist(x, bins = 20, color = "yellow") 
plt.title("Sepal Length in cm") 
plt.xlabel("Sepal_lenght_cm") 
plt.ylabel("Count")
plt.show()

#below is the same for fifferent variable
plt.figure(figsize = (10, 7)) 
x = df["petal_length"] 
plt.hist(x, bins = 20, color = "grey") 
plt.title("Petal Length in cm") 
plt.xlabel("Petal_lenght_cm") 
plt.ylabel("Count")
plt.show()

#below is the same for fifferent variable
plt.figure(figsize = (10, 7)) 
x = df["petal_width"] 
plt.hist(x, bins = 20, color = "brown") 
plt.title("Petal Width in cm") 
plt.xlabel("Petal_width_cm") 
plt.ylabel("Count")
plt.show()

#below is the same for fifferent variable
plt.figure(figsize = (10, 7)) 
x = df["species"] 
plt.hist(x, bins = 20, color = "blue") 
plt.title("Species") 
plt.xlabel("Type") 
plt.ylabel("Count")
plt.show()


#scatter plot can be created with Matplotlib. Data can be classified in several groups. My case: I add tile, labels
#
plt.scatter (df['sepal_length'], df['sepal_width'])
plt.title ("Sepal lenght and Sepal width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()
#A scatter plot is a type of plot that shows the data as a collection of points. The position of a point 
# depends on its two-dimensional value, where each value is a position on either the horizontal or vertical dimension.

#as above
plt.scatter (df['petal_length'], df['petal_width'])
plt.title ("Petal lenght and petal width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()

#finally, wonderful seaborn can make a scatter plot with possibility of several semantic groupings.
#Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface 
# for drawing attractive and informative statistical graphics. Thank you for seaborn. 

sns.pairplot (df, hue="species")
#df - dataframe (iris); hue is tring (variable name), in my case species 
# or plot a subset of variables:
sns.pairplot(df, vars=["sepal_width", "sepal_length"])
plt.show()

#based on that, the seaborn.pairplot will be enough to write the above programme, however I want to show my effort 
# and understanding the subject 





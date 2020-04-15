
#A programe that outputs a summary of each variable (from the Iris data set) to a 
# single text file,saves a histogram of each variable to png files, and
# outputs a scatter plot of each pair of variables.

#Before I start working with task, I need to import it (particular libraries)
#  into my Python environment.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import seaborn as sns


  #This opens a file object called text_file and creates a new indented block where we can read
  #  the contents of the opened file. 
#with open("iris.csv") as text_file:
 # for line in text_file.readlines():
 # print(text_file.read())
df = pd.read_csv("iris.csv")


plt.figure(figsize = (10, 7)) 
x = df["sepal_width"] 
plt.hist(x, bins = 20, color = "green") 
plt.title("Sepal Width in cm") 
plt.xlabel("Sepal_width_cm") 
plt.ylabel("Count")
plt.show()

plt.figure(figsize = (10, 7)) 
x = df["sepal_length"] 
plt.hist(x, bins = 20, color = "yellow") 
plt.title("Sepal Length in cm") 
plt.xlabel("Sepal_lenght_cm") 
plt.ylabel("Count")
plt.show()


plt.figure(figsize = (10, 7)) 
x = df["petal_length"] 
plt.hist(x, bins = 20, color = "grey") 
plt.title("Petal Length in cm") 
plt.xlabel("Petal_lenght_cm") 
plt.ylabel("Count")
plt.show()


plt.figure(figsize = (10, 7)) 
x = df["petal_width"] 
plt.hist(x, bins = 20, color = "brown") 
plt.title("Petal Width in cm") 
plt.xlabel("Petal_width_cm") 
plt.ylabel("Count")
plt.show()

plt.figure(figsize = (10, 7)) 
x = df["species"] 
plt.hist(x, bins = 20, color = "blue") 
plt.title("Species") 
plt.xlabel("Type") 
plt.ylabel("Count")
plt.show()

plt.scatter (df['sepal_length'], df['sepal_width'])
plt.title ("Sepal lenght and Sepal width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()


plt.scatter (df['petal_length'], df['petal_width'])
plt.title ("Petal lenght and petal width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()

sns.pairplot (df, hue="species")
plt.show()





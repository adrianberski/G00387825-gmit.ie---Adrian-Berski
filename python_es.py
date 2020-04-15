#A program that reads in a text file and outputs 
# the number of e's it contains. The program should 
# take the filename from an argument on the command line.


#The program reads the file called "moby-dick.txt".txt [attached to my github] 
#with the specific contents
with open("moby-dick.txt") as text_file:
  #This opens a file object called text_file and creates a new indented block where we can read
  #  the contents of the opened file. 
  text_data = text_file.read()
  #We then read the contents of the file text_file using 
  # text_file.read() and save the resulting string into the variable text_data. 
print(text_data)
#Then we print cool_contents, which outputs the statement
i = text_data.count("e")
#finally,I want to know how many times 'e' appears in this text, wIe can use the function count:
print(i)


# Program to create, write, and read a text file

# Creating and writing to the file
file = open("introduction.txt", "w")

file.write("My name is Kirti Katte.\n")
file.write("I am studying BCA at Hirachand Nemchand College of Commerce, Solapur.\n")
file.write("I am learning Python programming through my internship.")

file.close()

# Reading the file
file = open("introduction.txt", "r")

print("Contents of the file:\n")
print(file.read())

file.close()

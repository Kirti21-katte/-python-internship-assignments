# Program to demonstrate string operations

text = input("Enter a string: ")

print("Original String:", text)
print("Upper Case:", text.upper())
print("Lower Case:", text.lower())
print("Replace:", text.replace("Python", "Programming"))
print("Find:", text.find("Python"))


# Program to demonstrate list operations

numbers = [10, 30, 20, 50, 40]

print("Original List:", numbers)

numbers.append(80)
print("After Append:", numbers)

numbers.remove(50)
print("After Remove:", numbers)

numbers.sort()
print("After Sort:", numbers)


# Program to demonstrate tuple creation and indexing

animals= ("Dog", "Monkey", "Elephant", "Grasshoper")

print("Tuple:", animals)
print("First Element:", animals[0])
print("Second Element:", animals[2])
print("Last Element:", animals[-1])


# Program to store student information using a dictionary

student = {
    "Name": "Shivu",
    "College": "HNCC,Solapur ",
    "Branch": "MCA"
}

print("Student Information")
print("Name:", student["Name"])
print("College:", student["College"])
print("Branch:", student["Branch"])


# Program to demonstrate set operations

numbers = {10, 20, 30, 40}

print("Original Set:", numbers)

numbers.add(60)
print("After Add:", numbers)

numbers.remove(30)
print("After Remove:", numbers)

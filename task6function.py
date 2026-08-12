
# Function to calculate the square of a number
def square(number):
    return number * number

# Function to calculate the average of three numbers
def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

# Taking input from the user
num = int(input("Enter a number to find its square: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Calling the functions and displaying the results
print("\nResults")
print("Square of", num, "=", square(num))
print("Average of", a, ",", b, "and", c, "=", average(a, b, c))

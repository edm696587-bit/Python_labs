# Lab:
# 	- write a program that prints hello world
print("hello world")
# 	- application to take a number in binary form from the user, and print it as a decimal
try:
    binn = input(" Enter a binary number : ")
    decimal = int(binn,2)
    print("your binary number in decimal =  " ,decimal)
except:
    print("please inter a valid number")
# 	- write a function that takes a number as an argument and if the number
# 		divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 		divisible by both return "FizzBuzz"
def validate_number(num):
    if num %3 ==0 and num %5 ==0:
        return "FizzBuzz"
    elif num %3 ==0:
        return "Fizz"
    elif num % 5 == 0:
        return "buzz"    
    
    else :
        return "number you entered not divisible by 5 or 3 "
try:
    num = int(input(" Enter number to check : "))
    print(validate_number(num))
except:
    print("Enter a numeric value ")    

# 	- Ask the user to enter the radius of a circle print its calculated area and circumference
try:
    radius = float(input("Enter the radius of circle : "))
    Area = 3.14*radius**2
    circumference = 2 * 3.14 * radius
    print(f"the Area of your circle = {Area} and the circumference = {circumference}")
except:
    print("Enter a number")


# 	- Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data
try:
    name = input("Enter your name: ")
    if not name.strip() or name.isdigit():
        print("Invalid name. Please enter a valid name.")

    email = input("Enter your email: ")
    print("Name: ", name)
    print("Email: ", email)
except:
     print("please enter a valid name")

# 	- Write a program that prints the number of times the substring 'iti' occurs in a string

counter = 0
try:
    string = str(input("Enter a string to check the occarance of iti : "))
    for i in range(len(string)-2):     
        sub = string[i:i+3]
        if sub == "iti":
            counter +=1
    print(counter)
except:
    print("string not valid")             
                 
        



        

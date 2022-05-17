#Temperature Conversion (Fahrenheit) by Dominique Hill

#Get Text Information from User
name=input("Enter your name")

#Get numbers information from user
Celsius = eval(input("Enter Celsius Temperature"))

#Calculate Fahrenheit
Fahrenheit = (Celsius*1.8)+32

#Display Answer
print("Hello", name, "It's", Celsius, "degrees Celsius", "which is", Fahrenheit, "degrees Fahrenheit")

#if stqtement to print "wear a jacket, its cold outside, wear a jacket"
if Fahrenheit < 40:
    print("Hello", name, "wear a jacket, it's cold outside.")

#if statement to print "no need for a jacket today"
if Fahrenheit >60:
    print("Hello", name, "no need for a jacket today.")
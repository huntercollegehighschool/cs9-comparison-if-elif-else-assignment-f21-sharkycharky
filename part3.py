
#write your code below

number = int(input("Enter a number: "))

if number == 0: 
  print("zero")
elif number > 0 : 
  print("positive")
else: # linked to latest if statement
  print("Negative")

if number % 3 == 0: 
  print("Divisible by three")
else: # linked to latest if statement
  print("Not divisible by three")
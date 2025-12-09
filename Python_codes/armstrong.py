# write a progra to check given integer number is armstrong number or not
number = int(input("Enter the number : "))
original = number

total = 0
count = 0

while number != 0 : # this while loop to find length of given number
    number = number//10
    count = count + 1
# print("Count : ",count)


number = original

while number != 0 : # this loop to power the each number in the given number 
    total = total + (number%10)**count
    number = number//10

if total == original:
    print(f"{original} is a armstrong number")
else:
    print(f"{original} is not a armstrong number")
    

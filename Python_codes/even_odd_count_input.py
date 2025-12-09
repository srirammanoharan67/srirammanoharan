# write a program to print even numbers count and odd numbers count from the given integer number
number = 12345

odd_count = 0
even_count = 0

while number != 0:
    if(number%10)% 2 == 0:
        even_count+=1
    else:
        odd_count+=1
    number = number//10
print("Even count : ",even_count)
print("Odd count : ",odd_count)
        

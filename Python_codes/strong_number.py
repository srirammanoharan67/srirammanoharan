# wapt check the given integer number is strong number or not
number = int(input('Enter the number : '))
original = number

total = 0
while number != 0 :
    last_number = number%10
    fact = 1
    
    for i in range(1,last_number+1):
        fact = fact*i

    number = number//10
    total = total + fact
   
if total == original:
    print(f'{original} is a strong number')
else:
    print(f'{original} is not a strong number')

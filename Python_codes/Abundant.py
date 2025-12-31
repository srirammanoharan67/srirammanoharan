num = int(input("Enter the number : "))

def abundant_number(num):
    total = 0
    for i in range(1,num):
        if num%i == 0 :
            total = total + i
            
    return total > num

if num <= 0 :
    print('Less than zero is not allowed')

elif abundant_number(num):
    print(f'{num} is a abundant number')
else:
    print(f'{num} is not a abundant number')
    

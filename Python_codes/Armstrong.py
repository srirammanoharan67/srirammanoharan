num = int(input("Enter the armstrong number : "))

num_str = str(num)
length = len(num_str)

result = sum(int(i)**length for i in num_str)
if result == num :
    print(f"{num} is a armstrong number")
else:
    print(f"{num} is not an armstrong number")
    

# other Way to find Armstrong number 
num  = 153
copy = num

total = 0
length = 0

while copy > 0:
    copy = copy//10
    length = length  + 1
#print(length)

copy = num
while copy > 0 :
    total = total + (copy%10) ** length
    copy = copy//10

if num == total :
    print(f"{num} is a armstrong number")
else:
    print(f"{num} is not an armstrong number")
    

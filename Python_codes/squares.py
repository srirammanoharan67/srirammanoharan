# Generates squares using list comprehension
squares = [i*i for i in range(1,11)]
print(squares) # output : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Generates squares using for loop
for i in range(1,11):
    print(i*i,end=",") # output : 1,4,9,16,25,36,49,64,81,100,

# Generates squares using while loop
num = int(input("Enter the number of square : "))
i =1
while i <= num :
    print(i*i,end = ",") # output : 1,4,9,16,25,
    i+=1 # i = i + 1

# Generates squares using Lambda Function
square = lambda x : x**2
print(square(5))

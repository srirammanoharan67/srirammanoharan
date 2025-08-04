factor = 2
count  = 0
prime = int(input("Enter the number : "))

def prime_number(count, prime):
    while prime <= 1:
        print("Prime greater than 2")
        prime = int(input("Enter the number : "))
        
    for i in range(1, prime + 1):
        if prime % i == 0:
            count = count + 1
    return count == factor, prime  # also return the corrected prime

result, prime = prime_number(count, prime)

if result:
    print(f"{prime} is a prime number")
else:
    print(f"{prime} is not a prime number")

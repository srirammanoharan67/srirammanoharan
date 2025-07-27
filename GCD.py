num1 = 0
num2 = 0

def gcd_func(num1,num2):
    if num1 == 0 or num2 ==0 :
        return 
    if num1 > num2 :
        smallest = num2
    else :
        smallest = num1
    print("smallest : ",smallest)
    for i in range(1,smallest+1):
        if num1%i==0 and num2%i==0 :
            gcd = i
    return gcd
gcd_call = gcd_func(num1,num2)

if gcd_call:
    print(f"GCD of {num1} and {num2} is : {gcd_call}")
else :
    print("gcd numbers should be greater than or equal to 1")

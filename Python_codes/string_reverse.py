# Reverse a string using slicing
string = "python"
print(string[::-1])


# Reverse a string using recursion
def str_reverse(string):
    if not string:
        return string
    #Recursively call function with remaining string and add first index element at last
    return str_reverse(string[1:]) + string[0] 

string = "python"
print(str_reverse(string)) # output : nohtyp


# Reverse a string using for loop
string = "python"
reverse = ""
for i in string :
    reverse =  i + reverse # adding current char at last
print("Reversed string : ",reverse)


# Reverse a string using while loop
string = "python"
reverse = ""
i =0
while i < len(string):
    reverse = string[i] + reverse
    i+=1
print("Reversed string : ",reverse)

# Function to check if a string is a palindrome or not
def is_palindrome(s): 
    return text.lower() == s.lower()[::-1]

text = input("Enter text : ")
result = is_palindrome(text) # Output: True or False

if result :
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")

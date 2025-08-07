# Function to count vowels in a given string
def count_vowels(s):
     return sum(1 for char in s.lower() if char in "aeiou")
print(count_vowels("Hello World")) # Output: 3


# Function and list comprehension to count vowels in a given string
def count_vowels(s):
     return sum([1 for char in s.lower() if char in "aeiou"])
print(count_vowels("Hello World")) # Output: 3

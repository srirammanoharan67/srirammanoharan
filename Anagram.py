def is_anagram(ele_1,ele_2):
    if len(ele_1) != len(ele_2):
        return False

    if sorted(ele_1) == sorted(ele_2):
        print("Element 1 : ",sorted(ele_1))
        print("Element 2 : ",sorted(ele_2))
        return True

ele_1,ele_2 = input("Enter the elements : ").split() # User input


if is_anagram(ele_1,ele_2):  # Function calling and returning value
    print("{} and {} is an anagram".format(ele_1,ele_2))
else:
    print("{} and {} is not an anagram".format(ele_1,ele_2))
    
    

# Angram checker using sorted()
def check_anagram(s1, s2):
     #print(f"sorted  of s1 : {sorted(s1)}")
     #print(f"sorted  of s2 : {sorted(s2)}")
     return sorted(s1.lower()) == sorted(s2.lower())
print(check_anagram("listen", "silent")) # Output: True


# Angram checker using dictionary .get() function
def check_anagram(string):
     freq = {}
     for ch in string :
          freq[ch] = freq.get(ch,0) + 1
     return freq
print(check_anagram("listen")== check_anagram("silent"))

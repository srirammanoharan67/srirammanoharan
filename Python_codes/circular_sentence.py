string = "light tender rain near real lull"

class circular:
    def circular_string(self,text):
        if text[0] != text[-1]:
            return False
            
        for i in range(len(text)):
            if i == " " :
               if text[i-1] != text[i+1] :
                   return False
        return True
            
    
obj = circular()
result = obj.circular_string(string)
print(result)

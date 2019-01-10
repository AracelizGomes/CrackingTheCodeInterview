#URLify: write a method to replace all spaces in a string with "%20"

class URLify:
  def __init__(self, s):
    self.s = s.strip() #trim whitespace on end of string
  
  def helper(self, s):
    self.s = self.s.replace(" ", "20%") #replace all spaces with %20
    print(self.s)
    
s = (URLify("Mr John Smith   "))
s.helper(s)

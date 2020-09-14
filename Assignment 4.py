''' 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass. '''

class maintriangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.area = 0
        
class subtriangle(maintriangle):
    def __init__(self, a,b,c):
        maintriangle.__init__(self,a,b,c)
            
    def calculatearea(self):
        
        s = (self.a + self.b + self.c) / 2
        self.area = float((s * (s-self.a)* (s-self.b) *(s-self.c))) ** 0.5
        
    def getarea(self):
        return self.area
    
a,b,c = eval(input("a = ")), eval(input("b = ")), eval(input("c = "))
output = subtriangle(a,b,c)
output.calculatearea()
print("Area of",a,b,c,"sides is:",output.getarea())


''' 1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
the list of words that are longer than n.'''

def filter_long_words(lis,n):
    word_len = []
    txt = lis.split(" ")
    for i in txt:
        if len(i) > n:
            word_len.append(i)
    return word_len

list1 = input("Enter your string:")
number = int(input("Enter your number:"))
output = filter_long_words(list1,n)
print("The list of words which  are longer than",number,"are:",output)    

''' 2.1 Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
Here 2,3 and 4 are the lengths of the words in the list.'''

words = ["ab", "cde", "erty"]

def wordlength(words):
    return list(map(lambda x:len(x), words))

print((str(wordlength(words)))+" are the length of the words in the list "+str(words))

'''2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
it is a vowel, False otherwise.'''

def vowel(char):
    return_value = ""
    if(len(char) == 1):
        vow_list = ['a','e','i','o','u']
        if char.lower() in vow_list:
            return_value = "vowel"
        else:
            return_value = "not vowel"
    else:
        return_value="Kindly enter a character only"
    return return_value        

char_input = input("Enter your character:")
output2 = vowel(char_input)
print("The character",char_input,"is:",output2)

'''Write a function to compute 5/0 and use try/except to catch the exceptions.'''
#Defining function
def divdebyzero(a,b):
    try:
        a/b
    except ZeroDivisionError as z:
        print("The number",a,"cannot be divisible by zero\n An exception has occured as,",z,"action has been attempted")

#defining the numbers
num1,num2 = 5,0

#executing the function
divdebyzero(num1,num2)


'''2. Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].
Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
Output should come as below:
Americans play Baseball.
Americans play Cricket.
Americans watch Baseball.
Americans watch Cricket.
Indians play Baseball.
Indians play Cricket.
Indians watch Baseball.
Indians watch Cricket.'''

subjects=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

output = [(sub+" "+ver+" "+obj+".") for sub in subjects for ver in verbs for obj in objects]

print("Output:")
for i in output:
    print(i)

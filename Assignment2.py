''' 1.	Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

Solution:  '''

def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*", end=" ")
        print("\n")
    for i in range(n-1,0,-1):
        for j in range(1,i+1):
            print("*", end=" ")
        print("\n")

pattern(5)

'''2. Write a Python program to reverse a word after accepting the input from the user.
Solution: '''

word = input("Enter the word:")
output = word[::-1]
print(output)

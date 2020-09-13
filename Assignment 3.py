'''1.1 Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()'''

#defining a function that will print sum of numbers
def myreduce(number):
    
    num = list(range(1,number+1))
    sum1 = 0
    for i in num:
        sum1 += i
    print("The sum of",num,"elements are:",sum1)
  
n = int(input("Enter your number: ")) 

myreduce(n)

''' Same can be achieved by built in reduce() function as below'''

n1 = int(input("Enter your number: ")) 
num1 = list(range(1,n1+1))

from functools import reduce
sum2 = reduce((lambda x,y:x+y),num1)

print("The sum of",num1,"elements are:",sum2)


'''1.2 Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()'''

'''Defining myfilter function: 

To find even and odd numbers'''
number = int(input("Enter your number:"))
number_list = list(range(1,number+1))
def myfilter(num_list):
     even = []
     odd = []
     for i in num_list:
         if(i%2==0):
             even.append(i)
         else:
            odd.append(i)
             
     return even,odd
        
output = myfilter(number_list)
print("The list of numbers:",number_list)
print("List of even numbers: ",output[0])
print("List of odd numbers:",output[1])


'''Same can be achieved by in built Filter function'''

num = int(input("Enter your number:"))
num_list = list(range(1,num+1))

num_odd = list(filter((lambda x:x%2!=0),num_list))
num_even = list(filter((lambda x:x%2==0),num_list))

print("The list of numbers:",num_list)
print("The list of even numbers:",num_even)
print("The list of odd numbers:",num_odd)


''' 2. Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]  '''
word = "ACADGILD"
output = [i for i in list(word)]
print(output)

''''[x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] '''
word_2 = list('xyz')
output1 = [i*n for i in word_2 for n in range(1,5)]
print(output1)

'''['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz'] '''
output2 =[i*n for n in range(1,5) for i in word_2]
print(output2)

'''[[2], [3], [4], [3], [4], [5], [4], [5], [6]] '''
list1 = [2,3,4]
output3 = [[i+n] for i in list1 for n in range(0,3)]
print(output3)

'''[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]'''
list2 = [2,3,4,5]
output4 = [[i+n for n in range(0,4)] for i in list2]
print(output4)

'''[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]'''
list3 = [1,2,3]
output5 = [(b,a) for a in list3 for b in list3]
print(output5)

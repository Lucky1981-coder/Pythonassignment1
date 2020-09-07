'''Write a Python program to remove duplicates from a list.
Method 1 : Naive method
In naive method, we simply traverse the list and append the first occurrence of the element in new list and ignore all the other occurrences of that particular element. '''

#Initializing the list
sample_list = [1,2,2,3,4,5,7,7,8,9,10,10]
print ("The original list is : " +  str(sample_list)) 

output_list = []
#Using Naive method to remove duplicates from the list
for i in sample_list:
    if i not in output_list:
        output_list.append(i)
        
#Printing list after removing duplicates
print("The list after removing duplicates is: " + str(output_list))

''' Output:

The original list is : [1, 2, 2, 3, 4, 5, 7, 7, 8, 9, 10, 10]
The list after removing duplicates is: [1, 2, 3, 4, 5, 7, 8, 9, 10] '''

'''Method 2:  Using collections.OrderedDict.fromkeys()
This is fastest method to achieve the particular task. 
It first removes the duplicates and returns a dictionary which has to be converted to list. This works well in case of strings also. '''

# Using collections.OrderedDict.fromkeys() 
from collections import OrderedDict 

#Initializing the list
sample_list1 = [1,2,2,3,4,5,7,7,8,9,10,10]
print ("The original list is : " +  str(sample_list)) 

#Using collections.OrderedDict.fromkeys() to remove the duplicates from the list
output_list1 = list(OrderedDict.fromkeys(sample_list1))

#Printing list after removing duplicates
print("The list after removing duplicates is: " + str(output_list1))  
                    
''' Output:

The original list is : [1, 2, 2, 3, 4, 5, 7, 7, 8, 9, 10, 10]
The list after removing duplicates is: [1, 2, 3, 4, 5, 7, 8, 9, 10] '''


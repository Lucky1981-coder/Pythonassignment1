# Write a Python program to remove duplicates from a list.

sample_list = [1,2,2,3,4,5,7,7,8,9,10,10]
output_list = []
for i in sample_list:
    if i not in output_list:
        output_list.append(i)
        
output_list
    

#Task 2: Demonstrate List Slicing

mylist = []
for i in range(1,11):
    mylist.append(i)
print("Original List:" , mylist)
#Extracts the first five elements from the list.
extracted_values = mylist[0:5]
print("Extracted First five elements: ", extracted_values)
reverse_values = extracted_values.reverse()
print("Reversed Extracted Elements: ", extracted_values)
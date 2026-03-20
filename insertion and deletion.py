#Insertion and Deletion of Arrays

#Creating an array
arr = [15, 20, 25, 30, 35]
print("Original array:", arr)

#Insertion of an array
i = int(input("Insert position: "))
v = int(input("Value: "))
arr.insert(i,v)
print("After insert:", arr)

# Deletion 
d = int(input("Delete position: "))
arr.pop(d)
print("After delete:", arr)


import array

# INITIALIZE array with some values, i is the data type of array
arr = array.array('i', [1, 2, 3])
# printing original array, the end argument prevents from adding a new line after each print
print("INITIALIZE: the new created array is : ", end=" ")
for i in range(0, 3):
    print(arr[i], end=" ")
print("\r")
print("------ End-")

#TYPECODE: to print data type
print("typecode of the array is : ", end=" ")
print(arr.typecode, end=" ")
print("\r")
print("------ TYPECODE End-")


#ITEMSIZE: returns size of bytes of single array element
arr.append(1)
arr.append(2)
arr.append(5)
print("itemsize of the array is : ")
print(arr.itemsize)
print("\r")
print("------ ITEMSIZE End-")

#buffer_info(): returns tuple representing the address where array is stored and number of elements in it
print("Print buffer info of array is : ")
print(arr.buffer_info())
print("\r")
print("------ buffer_info() End-")

#count(): counts the number of occurence of argument
print("Print occurence of 1 in arr: ")
print(arr.count(1))
print("\r")
print("------ count() End-")

#extend(): append a whole array mentioned in arguments to a specified array
arr2 =  array.array('i', [7, 8, 9, 10])
print("appending arr by adding arr2")
arr.extend(arr2)

print("Modified array is : ", end=" ")
for i in range(len(arr)):
    print(arr[i], end=" ")
print("\r")
print("------ extend(): End-")

#Array fromlist(): appends a mentioned list to end of an array
arr3 = array.array('i', [7, 8, 9, 10])
li = [1,2,3,4]
#using fromlist() to append list to end of an array
arr3.fromlist(li)

print("arr3 with list li at end :" , end=" ")
for i in range(len(arr3)):
    print(arr3[i], end=" ")
print("\r")
print("------ fromlist() End-")

#tolist(): converts an array to list
li2 = arr3.tolist()

print("li3 which was converted from arr3 :" , end=" ")
for i in range(len(li2)):
    print(li2[i], end=" ")
print("\r")
print("------ fromlist() End-")
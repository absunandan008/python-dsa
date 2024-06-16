# import array
import array

# INITIALIZE array with some values, i is the data type of array
arr = array.array('i', [1,2,3])

# printing original array, the end argument prevents from adding a new line after each print
print("INITIALIZE: the new created array is : ", end=" ")
for i in range(0,3):
    print(arr[i], end=" ")
print("\r")
print("------ End-")

#APPEND: add an element at end of array
arr.append(4)

print("APPEND: Printing array after appending 4th element", end=" ")
for i in range(len(arr)):
    print(arr[i], end=" ")
print("\r")
print("------ APPEND End-")

#INSERT: insert an element at 3rd position and it increases the array size O(n) worst time
# and space complexity is O(n)
arr.insert(2,5)

#print array again
print("INSERT: new array after inserting is: ", end=" ")
for i in range(len(arr)):
    print(arr[i], end=" ")
print("\r")
print("------ INSERT End-")

#POP: remoce an element, it removes the said element from the given position
arr.pop(2)
print("POP: Printing array after pop : ", end=" ")
for i in range(len(arr)):
    print(arr[i], end=" ")
print("\r")
print("------ POP End-")

#REMOVE: array remove method, this is used to remove first occurence of the value
arr.remove(3)
print("REMOVE: Printing array after remove : ", end=" ")
for i in range(len(arr)):
    print(arr[i], end=" ")
print("\r")
print("------ REMOVE End-")

#adding extra members
arr.append(1)
arr.append(2)
arr.append(5)

#INDEX: array index method returns first occurence of the value
print("INDEX: Printing array after append : ", end=" ")
for i in range(len(arr)):
    print(arr[i], end=" ")
print("\r")
print("print first occurence of 2 :", end=" ")
print(arr.index(2), end=" ")
print("\r")
print("------ INDEX End-")

#REVERSE: this reverses the array
arr.reverse()
print("REVERSE: Printing array after reverse : ", end=" ")
for i in range(len(arr)):
    print(arr[i], end=" ")
print("\r")
print("------ REVERSE End-")

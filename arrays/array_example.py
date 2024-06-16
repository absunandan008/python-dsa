# import array
import array

# initialize array with some values, i is the data type of array
arr = array.array('i', [1,2,3])

# printing original array, the end argument prevents from adding a new line after each print
print("the new created array is : ", end=" ")
for i in range(0,3):
    print(arr[i], end=" ")
print("\r")
print("--")

#add an element at end of array
arr.append(4)

print("Printing array after appending 4th element", end=" ")
for i in range(len(arr)):
    print(arr[i], end=" ")
print("\r")
print("--")

#insert element at 3rd position
arr.insert(2,5)

#print array again
print("new array after inserting is: ", end=" ")
for i in range(len(arr)):
    print(arr[i], end=" ")
print("\r")
print("--")
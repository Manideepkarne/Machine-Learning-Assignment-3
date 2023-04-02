import numpy as np

#A. Create a random vector of size 15 with integers in the range 1-20
vec = np.random.randint(1, 21, 15)
print("Original Vector:")
print(vec)

# Reshape the vector to a 3 by 5 array
arr = vec.reshape((3, 5))
print("Reshaped Array:")
print(arr)

# Replace the max in each row with 0
arr[np.arange(len(arr)), np.argmax(arr, axis=1)] = 0
print("Max in each row replaced with 0:")
print(arr)

# Create a 2-dimensional array of size 4 x 3
arr_2d = np.zeros((4, 3), dtype=np.int32)
print("2D Array Shape:", arr_2d.shape)
print("2D Array Type:", type(arr_2d))
print("2D Array Data Type:", arr_2d.dtype)

#B. Define the square array and Compute the eigenvalues and right eigenvectors
A = np.array([[3, -2], [1, 0]])

eigenvalues, eigenvectors = np.linalg.eig(A)

# Print the results
print("Eigenvalues:", eigenvalues)
print("Right eigenvectors:")
print(eigenvectors)

#C. Compute the sum of the diagonal element of a given array.

arr = np.array([[0, 1, 2],
                [3, 4, 5]])

diag_sum = np.trace(arr)
print(diag_sum)

#D. To create a new shape to an array without changing its data, we can use the np.reshape() method.

arr = np.array([[1, 2],
                [3, 4],
                [5, 6]])

new_shape1 = arr.reshape(2, 3)
new_shape2 = arr.reshape(3, 2)

print(new_shape1)
print(new_shape2)

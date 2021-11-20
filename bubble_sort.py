# Bubble Sort Algorithm in Python

def bubbleSort(array):
    n = len(array)
 
    # Loop thru all array elements
    for i in range(n):
 
        # Loop thru the array from 0 to n-i-1
        for j in range(0, n-i-1):
            
            # Swap if value in adjacent element is less 
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
 
# Create an array for testing
array = [78, 63, 95, 29, 12]

# Call the function passing in your array 
bubbleSort(array)

# Output results
print("The array is now sorted: ")
for i in range(len(array)):
    print(array[i], end=' ')
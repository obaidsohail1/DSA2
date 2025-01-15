# Define the quicksort function
# This function sorts the array in-place using the quicksort algorithm
de quicksort(array, left, right):
    if left < right:  # Proceed if there are elements to sort
        # Partition the array and get the pivot index
        pivot_index = partition(array, left, right)
        # Recursively sort the left subarray (elements less than the pivot)
        quicksort(array, left, pivot_index - 1)
        # Recursively sort the right subarray (elements greater than the pivot)
        quicksort(array, pivot_index + 1, right)

# Define the partition function
# This function places the pivot in its correct position and rearranges elements
def partition(array, left, right):
    pivot = array[right - 1]  # Use the second-to-last element as the pivot
    i = left - 1  # Initialize the index for smaller elements
    for j in range(left, right - 1):  # Iterate through the array
        if array[j] <= pivot:  # Check if the current element is less than or equal to the pivot
            i += 1  # Increment the index for smaller elements
            array[i], array[j] = array[j], array[i]  # Swap the current element with the element at index i
    # Swap the pivot element with the element at index i + 1 to place it correctly
    array[i + 1], array[right - 1] = array[right - 1], array[i + 1]
    return i + 1  # Return the pivot index

# Define a list of words to be sorted alphabetically
words = ["banana", "apple", "cherry", "date", "grape", "fig", "elderberry"]

# Print the original list
print("Original list:", words)

# Call the quicksort function to sort the list
quicksort(words, 0, len(words))

# Print the sorted list
print("Sorted list:", words)

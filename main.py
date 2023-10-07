import time  # To calculate time


def GenerateArray(arraySize, shift):  # Function to generate
    # Generate the array
    lengthOfArray = arraySize
    tempArray = []
    for i in range(shift, lengthOfArray):
        tempArray.append(i)

    for i in range(0, shift):
        tempArray.append(i)

    return tempArray


array1 = GenerateArray(262144, 2)
start = time.time_ns()  # Calculate start time in nanoseconds


def findMax(arr, low, high):
    # If there is only one element left
    if low == high:
        return arr[low]

    # Find mid
    mid = low + (high - low) // 2

    # Check if mid reaches 0, and it is greater than the next element or not
    if mid == 0 and arr[mid] > arr[mid + 1]:
        return arr[mid]

    # Check if mid itself is maximum element
    if high > mid > 0 and arr[mid + 1] < arr[mid] and arr[mid] > arr[mid - 1]:
        return arr[mid]

    # Deciding the direction
    if arr[low] > arr[mid]:
        return findMax(arr, low, mid - 1)
    else:
        return findMax(arr, mid + 1, high)


print(findMax(array1, 0, len(array1) - 1))
end = time.time_ns()  # Calculate end time in nanoseconds
print(f"Time taken {end - start}ns")  # Calculate the time taken in nanoseconds

# CS6212-Project02
This is the Project02 of CS6212. 
## Problem Statement
Finding Max Number in Circular Shifted Array.
We are given an array A[1..n] of sorted integers that has been circularly shifted some positions to the right. For example, [35, 42, 5, 15, 27, 29] is a sorted array that has been circularly shifted 2 positions, while [27, 29, 35, 42, 5, 15] has been shifted 4 positions. We can obviously find the largest element in A in O(n) time. Describe an O(log n) algorithm.

## Theoretical Analysis
We have to find the largest number in a circularly shifted array in O(log n) time. Since the array is already sorted the best way to achieve O(log n) is to do Binary Search.

1.	Initialize two pointers ‘low’ and ‘high’, to find the first and last indices of the array.
2.	Check if there is only one element left in the array. 
3.	Find the middle index and check if the middle index is the largest value.
4.	Now check if the middle index is larger than the first or the last index.
5.	If the middle is greater than the first index, then call the function with low and mis-1 as the pointers.
6.	Otherwise, call the function with the mid+1 and high as the pointers.
This algorithm will run in O (log n) because this is a modified Binary Search algorithm.




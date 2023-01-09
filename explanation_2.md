# Search in a Rotated Sorted Array

To solve this problem the binary search was used with some modification to identify the pivot (which is the number where the array becomes unordered)

The Binary Search is a well known O(log n) time complexity search algorithm that only works with ordered arrays.

The space complexity for this problem is O(n), since we are dealing with an array that can have n-integer-elements. Four other integer variables were also used in the binary search algorithm, and they do not depends on the array size.

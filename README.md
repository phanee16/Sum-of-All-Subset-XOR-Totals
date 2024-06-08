# Sum-of-All-Subset-XOR-Totals
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.


## Let's go through the solution with an example of nums = [5, 1, 6].

We initialize n = len(nums) = 3 and total_sum = 0.
We start iterating over all possible subsets using the outer loop mask ranging from 0 (empty set) to 2^n - 1 = 7 (all elements included).

### For mask = 0 (binary representation 000), no elements are included in the subset. The inner loop calculates the XOR of the empty subset, which is 0. total_sum remains 0.
### For mask = 1 (binary representation 001), the subset contains only the last element 6. The inner loop calculates the XOR as follows:

subset_xor = 0 ^ 6 = 6
total_sum = 0 + 6 = 6


### For mask = 2 (binary representation 010), the subset contains only the second element 1. The inner loop calculates the XOR as follows:

subset_xor = 0 ^ 1 = 1
total_sum = 6 + 1 = 7


### For mask = 3 (binary representation 011), the subset contains the second and third elements 1 and 6. The inner loop calculates the XOR as follows:

subset_xor = 0 ^ 1 ^ 6 = 7
total_sum = 7 + 7 = 14


### For mask = 4 (binary representation 100), the subset contains only the first element 5. The inner loop calculates the XOR as follows:

subset_xor = 0 ^ 5 = 5
total_sum = 14 + 5 = 19


### For mask = 5 (binary representation 101), the subset contains the first and third elements 5 and 6. The inner loop calculates the XOR as follows:

subset_xor = 0 ^ 5 ^ 6 = 3
total_sum = 19 + 3 = 22


### For mask = 6 (binary representation 110), the subset contains the first and second elements 5 and 1. The inner loop calculates the XOR as follows:

subset_xor = 0 ^ 5 ^ 1 = 4
total_sum = 22 + 4 = 26


### For mask = 7 (binary representation 111), the subset contains all three elements 5, 1, and 6. The inner loop calculates the XOR as follows:

subset_xor = 0 ^ 5 ^ 1 ^ 6 = 2
total_sum = 26 + 2 = 28




After iterating over all possible subsets, total_sum = 28 is the XOR sum of all subsets.
The function returns total_sum = 28.

In this example, the XOR sum of all subsets of [5, 1, 6] is 28. 

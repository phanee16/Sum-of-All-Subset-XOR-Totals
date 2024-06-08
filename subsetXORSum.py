import itertools 
def subsetXORSum(nums):
    n = len(nums)
    total_sum = 0
    
    # Calculate the XOR sum of all subsets
    for mask in range(1 << n):  # Iterate over all possible subsets
        subset_xor = 0
        for i in range(n):
            if mask & (1 << i):  # Check if the i-th bit is set in the mask
                subset_xor ^= nums[i]
        total_sum += subset_xor
    
    return total_sum

#Python random code
def countPartitions(arr):
    total_sum = sum(arr)
    prefix_sum = 0
    count = 0
    
    # Iterate through the array to find partitions
    for i in range(len(arr) - 1):  # we don't need to check the last element
        prefix_sum += arr[i]
        suffix_sum = total_sum - prefix_sum
        
        if (prefix_sum - suffix_sum) % 2 == 0:
            count += 1
            
    return count

# Test cases
print(countPartitions([10, 10, 3, 7, 6]))  # Output: 4
print(countPartitions([1, 2, 2]))  # Output: 0
print(countPartitions([2, 4, 6, 8]))  # Output: 3


def find_zero_sum_triplets(nums):
    nums.sort()  # Sort the array
    n = len(nums)
    triplets = set()  # Use a set to avoid duplicate triplets
    
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # Skip duplicate elements
        
        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                triplets.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1  # Skip duplicate elements
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1  # Skip duplicate elements
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return list(triplets)

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
triplets = find_zero_sum_triplets(nums)
print("Unique triplets that sum to zero:")
for triplet in triplets:
    print(triplet)

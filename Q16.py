# Q16. Implement the Two Sum problem using a dictionary and return the indices of the two numbers whose sum equals the target.

# using dict -optimized way
def two_sum(nums, target): 
    seen = {}

    for i in range(len(nums)):

        needed = target - nums[i]

        if needed in seen:
            return [seen[needed], i]
        
        seen[nums[i]] = i
        print(seen)
       
    return []


nums = [2,7,4,15]
target = 6

print(two_sum(nums, target))

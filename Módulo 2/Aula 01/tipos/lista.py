nums = [1,2,3]
print(type(nums))
nums.append(3)
print(len(nums))

nums.append(3)
nums.append(5)
print(len(nums))

nums[3] = 100
nums.insert(0, -200)
print(nums)

print(nums[5])

# Array slice
print(nums[-1])
print(nums[1:5])
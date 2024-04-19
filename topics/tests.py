m = [1, 2, 3, 4, 4]
def rotate(nums, k):
    global m
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]

rotate(m, 1)
print(f"m = {m}")

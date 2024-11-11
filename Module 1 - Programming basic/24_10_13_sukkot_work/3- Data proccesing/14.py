# 14
nums: list[int] = []
for _ in range(5):
    nums.append(int(input("Enter a num: ")))
avg_nums = sum(nums) / len(nums)
print(f"avg: {avg_nums}")
print([num for num in nums if num > avg_nums])
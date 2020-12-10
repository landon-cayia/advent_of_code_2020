def part1(nums, low, high):
    current_val = 0
    while current_val == 0:
        current_val = check_sums(nums, low, high)
        low += 1
        high += 1
    return current_val


def check_sums(nums, low, high):
    for i in nums[low:high]:
        for j in [k for k in nums[low:high] if k != i]:
            if i + j == nums[high]:
                return 0
    return nums[high]


with open('input/input_12-09-20.txt') as f:
    data = f.readlines()


number_list = [int(num) for num in data]
low_idx = 0
high_idx = 25
print(part1(number_list, low_idx, high_idx))

def part1(jolts):
    curr_rating = 0  # charging outlet jolt rating = 0
    diffs = {1: 0, 2: 0, 3: 1}  # diff of 3 initialized to 1 since device joltage will produce a diff of 3
    while curr_rating < max(jolts):
        compatible_js = [curr_rating + 1, curr_rating + 2, curr_rating + 3]
        for j in compatible_js:
            if j in jolts:
                d = j - curr_rating
                diffs[d] += 1
                curr_rating = j
                break
    ans = diffs[1] * diffs[3]
    return ans


with open('input/input_12-10-20.txt', 'r') as f:
    data = f.readlines()

jolt_list = [int(jolt) for jolt in data]
ans1 = part1(jolt_list)
print(ans1)

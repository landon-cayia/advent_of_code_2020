with open('input/input_12-07-20.txt', 'r') as f:
    data = [s.rstrip('.') for s in f.read().split('\n')]

bags = [[e.strip().split() for e in b.split(',')] for b in data]

all_rules = []

for b in bags:
    num_rules = len(b)
    bag_rule_color = b[0][0] + ' ' + b[0][1]
    bag_rule_contents = []
    if b[0][4] != 'no':
        bag_rule_contents.append({int(b[0][4]): b[0][5] + ' ' + b[0][6]})
    for i in range(1, num_rules):
        bag_rule_contents.append({int(b[i][0]): b[i][1] + ' ' + b[i][2]})
    all_rules.append({bag_rule_color: bag_rule_contents})

count_options = 0

for r in all_rules:
    for key, value in r.items():
        for i in value:
            if list(i.values())[0] == 'shiny gold':
                count_options += 1
                break

print(count_options)

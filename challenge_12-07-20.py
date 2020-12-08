with open('input/input_12-07-20.txt', 'r') as f:
    data = f.readlines()

all_rules = {}

for rule in data:
    bag, contents = rule.split(' bags contain ')
    contents = contents.split(',')
    bag_rules = []
    for content in contents:
        content = content.split()
        color = content[1] + ' ' + content[2]
        bag_rules.append((content[0], color))
    all_rules[bag] = bag_rules

count_options = 0
new_options = -1
colors_to_check = ['shiny gold']
found_colors = []

while new_options != 0:
    new_options = 0
    new_colors_to_check = []
    for rule in all_rules:
        for item in all_rules[rule]:
            if item[1] in colors_to_check and rule not in found_colors:
                new_options += 1
                new_colors_to_check.append(rule)
                found_colors.append(rule)
    count_options += new_options
    colors_to_check.clear()
    colors_to_check = new_colors_to_check

print(count_options)

acc1 = 0


def parse_code(c):
    code_list = []
    for line in c:
        command, value = line.split()
        op = value[0]
        number = int(value[1:])
        code_list.append((command, op, number))
    return code_list


def exec_instr(line, cmd, op, num):
    global acc1
    if cmd == 'acc':
        if op == '+':
            acc1 += num
            line += 1
            return line
        elif op == '-':
            acc1 -= num
            line += 1
            return line
    elif cmd == 'jmp':
        if op == '+':
            line += num
            return line
        elif op == '-':
            line -= num
            return line
    elif cmd == 'nop':
        line += 1
        return line


with open('input/input_12-08-20.txt', 'r') as f:
    data = f.readlines()


def part1(code1):
    reached_lines = []
    curr_line = 0
    while curr_line not in reached_lines:
        next_line = exec_instr(curr_line, code1[curr_line][0], code1[curr_line][1], code1[curr_line][2])
        reached_lines.append(curr_line)
        curr_line = next_line
    return curr_line


code = parse_code(data)
part1(code)
print(acc1)

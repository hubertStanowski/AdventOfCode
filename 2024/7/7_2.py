import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')

data = []
with open(input_path) as f:
    for line in f.read().split('\n'):
        target, equation = line.split(':')
        data.append((int(target), list(map(int, equation.split()))))


def evaluate(target, equation, i, curr):
    if i == len(equation):
        return curr == target

    return (evaluate(target, equation, i + 1, curr + equation[i]) or
            evaluate(target, equation, i + 1, curr * equation[i]) or
            evaluate(target, equation, i + 1, int(str(curr) + str(equation[i]))))


part2 = 0
for (target, equation) in data:
    if evaluate(target, equation, 1, equation[0]):
        part2 += target

print("PART 2: ", part2)

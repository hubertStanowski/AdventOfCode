import os
import math
from collections import deque
from collections import defaultdict


def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, 'input.txt')

    data = []
    with open(input_path) as f:
        data = f.read().split('\n\n')
        data[0] = data[0].replace("Register A: ", "").replace(
            "Register B: ", "").replace("Register C: ", "").split("\n")
        registers = {
            "A": int(data[0][0]),
            "B": int(data[0][1]),
            "C": int(data[0][2])
        }
        data[0] = registers
        data[1] = list(map(int, data[1].replace("Program: ", "").split(",")))

    return data


def get_combo(registers, operand):
    if operand == 4:
        return registers['A']
    if operand == 5:
        return registers['B']
    if operand == 6:
        return registers['C']
    return operand


def part1(data):
    input_registers, program = data
    registers = {key: val for key, val in input_registers.items()}

    i = 0
    result = []
    while i < len(program):
        opcode, operand = program[i:i+2]
        combo = get_combo(registers, operand)
        match opcode:
            case 0:
                registers['A'] >>= combo
            case 1:
                registers['B'] ^= operand
            case 2:
                registers['B'] = combo % 8
            case 3:
                if registers['A']:
                    i = operand - 2
            case 4:
                registers['B'] ^= registers['C']
            case 5:
                result.append(combo % 8)
            case 6:
                registers['B'] = registers['A'] >> combo
            case 7:
                registers['C'] = registers['A'] >> combo
        i += 2

    return result


def part2(data):
    input_registers, program = data

    def run_program(a):
        registers = dict(A=a, b=input_registers["B"], c=input_registers["C"])
        i = 0
        result = []
        while i < len(program):
            opcode, operand = program[i:i+2]
            combo = get_combo(registers, operand)
            match opcode:
                case 0:
                    registers['A'] >>= combo
                case 1:
                    registers['B'] ^= operand
                case 2:
                    registers['B'] = combo % 8
                case 3:
                    if registers['A']:
                        i = operand
                        continue
                case 4:
                    registers['B'] ^= registers['C']
                case 5:
                    result.append(combo % 8)
                case 6:
                    registers['B'] = registers['A'] >> combo
                case 7:
                    registers['C'] = registers['A'] >> combo
            i += 2

        return result

    result = 0
    for i in reversed(range(len(program))):
        result <<= 3
        while run_program(result) != program[i:]:
            result += 1

    return result


if __name__ == "__main__":
    data = load_data()
    print("Part 1:", ",".join(map(str, part1(data))))
    print("Part 2:", part2(data))

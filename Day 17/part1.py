
def run_program(program, reg_a, reg_b, reg_c):
    # Registers A, B, C
    registers = {'A': reg_a, 'B': reg_b, 'C': reg_c}
    instruction_pointer = 0
    output = []

    # Resolve combo operand
    def resolve_combo_operand(operand):
        if operand in [0, 1, 2, 3]:
            return operand  # literal values
        elif operand == 4:
            return registers['A']
        elif operand == 5:
            return registers['B']
        elif operand == 6:
            return registers['C']
        else:
            raise ValueError("Invalid combo operand: 7 encountered")

    # Program Execution Loop
    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        instruction_pointer += 2  # By default, move to next instruction

        if opcode == 0:  # adv - A = A // (2 ** resolve_combo_operand(operand))
            denominator = 2 ** resolve_combo_operand(operand)
            registers['A'] //= denominator
        elif opcode == 1:  # bxl - B = B ^ operand
            registers['B'] ^= operand
        elif opcode == 2:  # bst - B = resolve_combo_operand(operand) % 8
            registers['B'] = resolve_combo_operand(operand) % 8
        elif opcode == 3:  # jnz - Jump if A != 0
            if registers['A'] != 0:
                instruction_pointer = operand
        elif opcode == 4:  # bxc - B = B ^ C (operand ignored)
            registers['B'] ^= registers['C']
        elif opcode == 5:  # out - Output resolve_combo_operand(operand) % 8
            output.append(resolve_combo_operand(operand) % 8)
        elif opcode == 6:  # bdv - B = A // (2 ** resolve_combo_operand(operand))
            denominator = 2 ** resolve_combo_operand(operand)
            registers['B'] = registers['A'] // denominator
        elif opcode == 7:  # cdv - C = A // (2 ** resolve_combo_operand(operand))
            denominator = 2 ** resolve_combo_operand(operand)
            registers['C'] = registers['A'] // denominator
        else:
            raise ValueError(f"Unknown opcode: {opcode}")

    return ",".join(map(str, output))


if __name__ == "__main__":
    # Read input from file
    with open("inputPart1.txt", "r") as file:
        lines = [line.strip() for line in file]

    # Parse initial register values
    reg_a = int(lines[0].split(":")[1].strip())
    reg_b = int(lines[1].split(":")[1].strip())
    reg_c = int(lines[2].split(":")[1].strip())

    # Parse the program (list of integers)
    program = list(map(int, lines[4].split(":")[1].strip().split(",")))

    # Run the program and collect the output
    result = run_program(program, reg_a, reg_b, reg_c)
    print("Output:", result)


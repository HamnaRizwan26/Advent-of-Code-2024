def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def find_solution(a1, a2, b1, b2, target_x, target_y):
    print(f"\nSolving for equations:")
    print(f"{a1}A + {b1}B = {target_x}")
    print(f"{a2}A + {b2}B = {target_y}")

    # Calculate determinant
    det = a1 * b2 - a2 * b1

    if det == 0:
        print("No solution - equations are dependent")
        return None

    # Using Cramer's rule
    n = (target_x * b2 - target_y * b1) / det
    m = (a1 * target_y - a2 * target_x) / det

    # Check if solution is integer and non-negative
    if n != int(n) or m != int(m) or n < 0 or m < 0:
        print(f"No valid solution: A={n}, B={m}")
        return None

    n = int(n)
    m = int(m)

    # Verify solution
    if (a1 * n + b1 * m == target_x) and (a2 * n + b2 * m == target_y):
        print(f"Found solution: A={n}, B={m}")
        return (n, m)

    return None

def solve_claw_machines_part2(input_data):
    total_tokens = 0
    possible_prizes = 0
    OFFSET = 10000000000000

    lines = input_data.strip().split('\n')

    for i in range(0, len(lines), 4):
        if i + 2 >= len(lines):
            break

        print(f"\nProcessing Machine {i//4 + 1}")

        # Parse input
        a_line = lines[i].strip()
        ax = int(a_line[a_line.find('X+')+2:a_line.find(',')])
        ay = int(a_line[a_line.find('Y+')+2:])

        b_line = lines[i+1].strip()
        bx = int(b_line[b_line.find('X+')+2:b_line.find(',')])
        by = int(b_line[b_line.find('Y+')+2:])

        p_line = lines[i+2].strip()
        px = int(p_line[p_line.find('X=')+2:p_line.find(',')]) + OFFSET
        py = int(p_line[p_line.find('Y=')+2:]) + OFFSET

        print(f"Button A: X+{ax}, Y+{ay}")
        print(f"Button B: X+{bx}, Y+{by}")
        print(f"Prize: X={px}, Y={py}")

        # Find solution
        solution = find_solution(ax, ay, bx, by, px, py)

        if solution:
            n, m = solution
            tokens = 3 * n + m
            total_tokens += tokens
            possible_prizes += 1
            print(f"Solution found for Machine {i//4 + 1}:")
            print(f"Button A presses: {n}")
            print(f"Button B presses: {m}")
            print(f"Tokens needed: {tokens}")
        else:
            print(f"No solution found for Machine {i//4 + 1}")

    return total_tokens, possible_prizes

def main(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read()

    total_tokens, possible_prizes = solve_claw_machines_part2(input_data)

    print("\nFinal Results:")
    print(f"Total possible prizes: {possible_prizes}")
    print(f"Total tokens needed: {total_tokens}")

# Run the solution with the input file
main("inputPart2.txt")

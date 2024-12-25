def calculate_resonant_harmonics(antenna_map):
    """
    Calculate the total number of unique locations containing an antinode,
    considering the effect of resonant harmonics.
    """
    rows = len(antenna_map)
    cols = len(antenna_map[0])
    antennas = {}

    # Collect all antenna positions and their frequencies
    for r in range(rows):
        for c in range(cols):
            freq = antenna_map[r][c]
            if freq != '.':  # Only consider antennas
                if freq not in antennas:
                    antennas[freq] = []
                antennas[freq].append((r, c))

    antinodes = set()

    # Process each frequency
    for freq, positions in antennas.items():
        n = len(positions)

        # Add all antenna positions as antinodes
        for pos in positions:
            antinodes.add(pos)

        # Calculate all positions in line with two antennas
        for i in range(n):
            for j in range(i + 1, n):
                r1, c1 = positions[i]
                r2, c2 = positions[j]

                # Calculate differences
                dr = r2 - r1
                dc = c2 - c1

                # Calculate greatest common divisor for steps
                gcd = abs(dr) if dc == 0 else abs(dr) if dr == 0 else abs(__import__('math').gcd(dr, dc))
                step_r, step_c = dr // gcd, dc // gcd

                # Trace the line in both directions
                current_r, current_c = r1, c1
                while 0 <= current_r < rows and 0 <= current_c < cols:
                    antinodes.add((current_r, current_c))
                    current_r += step_r
                    current_c += step_c

                current_r, current_c = r1 - step_r, c1 - step_c
                while 0 <= current_r < rows and 0 <= current_c < cols:
                    antinodes.add((current_r, current_c))
                    current_r -= step_r
                    current_c -= step_c

    return len(antinodes)

# Read input from file
def read_input_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Main execution
if __name__ == "__main__":
    input_file = "inputPart2.txt"  # Replace with the path to your input file
    antenna_map = read_input_file(input_file)
    result = calculate_resonant_harmonics(antenna_map)
    print(f"Total unique antinode locations: {result}")

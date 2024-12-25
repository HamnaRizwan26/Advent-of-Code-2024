def calculate_antinodes(antenna_map):
    """
    Calculate the number of unique antinodes created by antennas in the map.
    """
    rows = len(antenna_map)
    cols = len(antenna_map[0])
    antennas = {}

    # Collect all antenna positions and their frequencies
    for r in range(rows):
        for c in range(cols):
            freq = antenna_map[r][c]
            if freq != '.':  # Only consider antenna positions
                if freq not in antennas:
                    antennas[freq] = []
                antennas[freq].append((r, c))

    antinodes = set()

    # Calculate antinodes for each frequency
    for freq, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(n):
                if i != j:
                    r1, c1 = positions[i]
                    r2, c2 = positions[j]

                    # Calculate differences
                    dr = r2 - r1
                    dc = c2 - c1

                    # Antinode 1 (outside the first antenna)
                    r_antinode1 = r1 - dr
                    c_antinode1 = c1 - dc

                    # Antinode 2 (outside the second antenna)
                    r_antinode2 = r2 + dr
                    c_antinode2 = c2 + dc

                    # Add valid antinodes within bounds
                    if 0 <= r_antinode1 < rows and 0 <= c_antinode1 < cols:
                        antinodes.add((r_antinode1, c_antinode1))
                    if 0 <= r_antinode2 < rows and 0 <= c_antinode2 < cols:
                        antinodes.add((r_antinode2, c_antinode2))

    return len(antinodes)

# Read input from file
def read_input_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Main execution
if __name__ == "__main__":
    input_file = "inputPart1.txt"  # Replace with your input file path
    antenna_map = read_input_file(input_file)
    result = calculate_antinodes(antenna_map)
    print(f"Part 1: Number of unique antinode locations: {result}")

def count_possible_designs(input_file):
    with open(input_file, 'r') as file:
        lines = file.read().strip().split('\n')

    # First line contains the available towel patterns
    towel_patterns = lines[0].split(', ')
    towel_set = set(towel_patterns)

    # Remaining lines after the blank line are the desired designs
    designs = lines[2:]

    def is_design_possible(design):
        # Use dynamic programming to check if the design can be formed
        dp = [False] * (len(design) + 1)
        dp[0] = True  # Base case: empty design is always possible

        for i in range(1, len(design) + 1):
            for pattern in towel_set:
                if dp[i - len(pattern)] and design[i - len(pattern):i] == pattern:
                    dp[i] = True
                    break
        return dp[-1]

    # Count possible designs
    possible_count = sum(1 for design in designs if is_design_possible(design))
    return possible_count

# Example usage
input_file = 'inputPart1.txt'
result = count_possible_designs(input_file)
print(f"Number of possible designs: {result}")

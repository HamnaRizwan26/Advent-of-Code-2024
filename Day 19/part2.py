def count_towel_arrangements(input_file):
    with open(input_file, 'r') as file:
        lines = file.read().strip().split('\n')

    # First line contains the available towel patterns
    towel_patterns = lines[0].split(', ')
    towel_set = set(towel_patterns)

    # Remaining lines after the blank line are the desired designs
    designs = lines[2:]

    def count_ways_to_form_design(design):
        # Use dynamic programming to count arrangements
        dp = [0] * (len(design) + 1)
        dp[0] = 1  # Base case: 1 way to form an empty design

        for i in range(1, len(design) + 1):
            for pattern in towel_set:
                if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                    dp[i] += dp[i - len(pattern)]

        return dp[-1]

    # Sum up the number of arrangements for all designs
    total_arrangements = sum(count_ways_to_form_design(design) for design in designs)
    return total_arrangements

# Example usage
input_file = 'inputPart2.txt'
result = count_towel_arrangements(input_file)
print(f"Total number of ways to arrange the designs: {result}")

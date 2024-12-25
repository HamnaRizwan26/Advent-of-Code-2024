# Define the function to compute the 2000th secret number for a given initial secret
def calculate_2000th_secret(initial_secret):
    MODULO = 16777216  # Modulo value for pruning
    secret = initial_secret

    # Generate the sequence up to the 2000th secret number
    for _ in range(2000):
        secret = (secret ^ (secret * 64)) % MODULO
        secret = (secret ^ (secret // 32)) % MODULO
        secret = (secret ^ (secret * 2048)) % MODULO

    return secret

# Main function to process the input file and calculate the result
def monkey_market_sum(filename="inputPart1.txt"):
    with open(filename, "r") as file:
        initial_secrets = [int(line.strip()) for line in file.readlines()]

    # Calculate the sum of the 2000th secret numbers
    result_sum = sum(calculate_2000th_secret(secret) for secret in initial_secrets)

    return result_sum

# Run the program and output the result
if __name__ == "__main__":
    output = monkey_market_sum("inputPart1.txt")
    print(f"Sum of the 2000th secret numbers: {output}")
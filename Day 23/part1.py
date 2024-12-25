# Efficient solution to solve the LAN Party problem
from collections import defaultdict

def read_input(file_name):
    """Reads input from the specified file."""
    with open(file_name, 'r') as file:
        connections = [line.strip().split('-') for line in file]
    return connections

def find_triangles(connections):
    """Finds all triangles in the graph."""
    # Build the adjacency list
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)

    triangles = set()

    # Detect triangles
    for node in graph:
        for neighbor in graph[node]:
            # Check intersection of neighbors to find a common third node
            common_neighbors = graph[node].intersection(graph[neighbor])
            for cn in common_neighbors:
                # Sort to ensure uniqueness of triangle representation
                triangle = tuple(sorted([node, neighbor, cn]))
                triangles.add(triangle)

    return triangles

def count_target_triangles(triangles):
    """Counts triangles containing at least one node starting with 't'."""
    return sum(1 for triangle in triangles if any(node.startswith('t') for node in triangle))

def main():
    # Input file name
    input_file = "inputPart1.txt"

    # Read input connections
    connections = read_input(input_file)

    # Find all triangles
    triangles = find_triangles(connections)

    # Count triangles with at least one node starting with 't'
    result = count_target_triangles(triangles)

    print(f"Number of target triangles: {result}")

if __name__ == "__main__":
    main()

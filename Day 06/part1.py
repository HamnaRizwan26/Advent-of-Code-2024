def step():
    return {
        "up": {"x": 0, "y": -1, "turn": "right"},
        "down": {"x": 0, "y": 1, "turn": "left"},
        "left": {"x": -1, "y": 0, "turn": "up"},
        "right": {"x": 1, "y": 0, "turn": "down"},
    }

def test(map_data, current, add=None):
    visited = set()
    turns = set()
    steps = step()
    
    if add:
        map_data[add["y"]][add["x"]] = "#"
    map_data[current["y"]][current["x"]] = "."

    while current["y"] >= 0 and current["y"] < len(map_data) and \
          current["x"] >= 0 and current["x"] < len(map_data[0]) and \
          map_data[current["y"]][current["x"]] in (".", "^"):
        
        next_pos = current.copy()
        
        while 0 <= next_pos["y"] < len(map_data) and \
              0 <= next_pos["x"] < len(map_data[0]) and \
              map_data[next_pos["y"]][next_pos["x"]] == ".":
            if not add:
                visited.add(f"{next_pos['x']},{next_pos['y']}")
            next_pos["x"] += steps[current["direction"]]["x"]
            next_pos["y"] += steps[current["direction"]]["y"]
        
        if 0 <= next_pos["y"] < len(map_data) and \
           0 <= next_pos["x"] < len(map_data[0]) and \
           map_data[next_pos["y"]][next_pos["x"]] == "#":
            next_pos["x"] -= steps[current["direction"]]["x"]
            next_pos["y"] -= steps[current["direction"]]["y"]
            next_pos["direction"] = steps[current["direction"]]["turn"]
            if f"{next_pos['x']},{next_pos['y']},{next_pos['direction']}" in turns:
                return turns
            turns.add(f"{next_pos['x']},{next_pos['y']},{next_pos['direction']}")
        
        current = next_pos
    
    return visited if not add else None

def parse(input_data):
    map_data = [list(line) for line in input_data.strip().split("\n")]
    start_y = next(i for i, line in enumerate(map_data) if "^" in line)
    start_x = map_data[start_y].index("^")
    current = {"x": start_x, "y": start_y, "direction": "up"}
    return map_data, current

def part1(input_data):
    map_data, current = parse(input_data)
    return len(test(map_data, current))

if __name__ == "__main__":
    # Read input from inputPart1.txt
    with open("inputPart1.txt", "r") as file:
        input_data = file.read()
    
    # Compute and print the result
    result = part1(input_data)
    print(f"Distinct positions visited: {result}")

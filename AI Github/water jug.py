from collections import deque

# Function to perform BFS and find the solution
def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    # Queue for storing the state of the jugs and the path taken to reach that state
    queue = deque()
    # Set for storing visited states
    visited = set()
    
    # Initial state: both jugs are empty, path starts with an empty list
    queue.append((0, 0, []))
    visited.add((0, 0))
    
    while queue:
        jug1, jug2, path = queue.popleft()
        
        # If we reach the target amount in either of the jugs
        if jug1 == target or jug2 == target:
            path.append((jug1, jug2))
            return path
        
        # List of possible moves
        possible_moves = [
            (jug1_capacity, jug2, "Fill Jug 1"),       # Fill Jug1
            (jug1, jug2_capacity, "Fill Jug 2"),       # Fill Jug2
            (0, jug2, "Empty Jug 1"),                  # Empty Jug1
            (jug1, 0, "Empty Jug 2"),                  # Empty Jug2
            (max(jug1 - (jug2_capacity - jug2), 0),    # Pour Jug1 -> Jug2
             min(jug2_capacity, jug2 + jug1), "Pour Jug1 to Jug2"),
            (min(jug1_capacity, jug1 + jug2),          # Pour Jug2 -> Jug1
             max(jug2 - (jug1_capacity - jug1), 0), "Pour Jug2 to Jug1")
        ]
        
        for new_jug1, new_jug2, action in possible_moves:
            if (new_jug1, new_jug2) not in visited:
                visited.add((new_jug1, new_jug2))
                queue.append((new_jug1, new_jug2, path + [(jug1, jug2, action)]))
    
    # If no solution is found
    return "No solution possible"

# Example usage
jug1_capacity = 2
jug2_capacity = 1
target = 2

solution_path = water_jug_bfs(jug1_capacity, jug2_capacity, target)

if solution_path == "No solution possible":
    print(solution_path)
else:
    print("Steps to reach the goal:")
    for (jug1, jug2, action) in solution_path:
        print(f"{action}: Jug1 = {jug1}, Jug2 = {jug2}")

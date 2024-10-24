# Steepest Ascent Hill Climbing Algorithm
def steepest_ascent_hill_climbing(start_state):
    current_state = start_state
    while True:
        current_distance = manhattan_distance(current_state)
        neighbors = get_neighbors(current_state)
        
        # Find the neighbor with the best (lowest) heuristic value
        next_state = min(neighbors, key=manhattan_distance)
        next_distance = manhattan_distance(next_state)

        if next_distance >= current_distance:  # No improvement
            return current_state

        current_state = next_state

# Example usage
start_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
solution = steepest_ascent_hill_climbing(start_state)
print("Solution State:")
for i in range(0, 9, 3):
    print(solution[i:i+3])

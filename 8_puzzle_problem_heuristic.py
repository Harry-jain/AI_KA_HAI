import heapq

goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def manhattan_distance(state):
    return sum(abs(i // 3 - goal_state.index(tile) // 3) + abs(i % 3 - goal_state.index(tile) % 3) 
               for i, tile in enumerate(state) if tile)

def get_neighbors(state):
    zero_idx = state.index(0)
    row, col = divmod(zero_idx, 3)
    neighbors, moves = [], [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in moves:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_idx = nr * 3 + nc
            new_state = state[:]
            new_state[zero_idx], new_state[new_idx] = new_state[new_idx], new_state[zero_idx]
            neighbors.append(new_state)
    return neighbors

def astar(start_state):
    open_list, closed_set = [], set()
    heapq.heappush(open_list, (manhattan_distance(start_state), 0, start_state, []))
    
    while open_list:
        _, g, state, path = heapq.heappop(open_list)
        if state == goal_state:
            return path + [state]
        closed_set.add(tuple(state))
        for neighbor in get_neighbors(state):
            if tuple(neighbor) not in closed_set:
                heapq.heappush(open_list, (g + 1 + manhattan_distance(neighbor), g + 1, neighbor, path + [state]))
    return None

# Example
start_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
solution_path = astar(start_state)

for step in solution_path:
    for i in range(0, len(step), 3):
        print(step[i:i+3])
    print()

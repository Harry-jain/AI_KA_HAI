from collections import deque

def min_operations(m, n, d):
    # Check if it's possible to measure d liters
    if d > n:
        return -1
    if d % gcd(m, n) != 0:
        return -1
    
    # To store the visited states
    visited = set()
    
    # Queue for BFS: (current_water_in_jug1, current_water_in_jug2, steps)
    queue = deque([(0, 0, 0)])
    
    while queue:
        x, y, steps = queue.popleft()
        
        # If either jug contains exactly d liters, return the steps
        if x == d or y == d:
            return steps
        
        # Skip if this state is already visited
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        # Possible operations:
        # 1. Fill Jug1 (m liters)
        queue.append((m, y, steps + 1))
        
        # 2. Fill Jug2 (n liters)
        queue.append((x, n, steps + 1))
        
        # 3. Empty Jug1
        queue.append((0, y, steps + 1))
        
        # 4. Empty Jug2
        queue.append((x, 0, steps + 1))
        
        # 5. Pour water from Jug1 to Jug2
        pour_to_jug2 = min(x, n - y)  # max water we can pour
        queue.append((x - pour_to_jug2, y + pour_to_jug2, steps + 1))
        
        # 6. Pour water from Jug2 to Jug1
        pour_to_jug1 = min(y, m - x)  # max water we can pour
        queue.append((x + pour_to_jug1, y - pour_to_jug1, steps + 1))
    
    # If no solution found
    return -1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
m = 3  # Jug1 capacity
n = 5  # Jug2 capacity
d = 4  # Desired amount of water

result = min_operations(m, n, d)
print(f"Minimum number of operations: {result}")

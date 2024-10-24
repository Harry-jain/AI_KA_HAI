# BY DFS METHOD

from math import gcd

def min_operations(m, n, d):
    # Check if it's possible to measure d liters
    if d > n:
        return -1
    if d % gcd(m, n) != 0:
        return -1
    
    # DFS initialization
    stack = [((0, 0), [])]
    visited = set()
    visited.add((0, 0))
    min_steps = float('inf')
    result_steps = None

    while stack:
        (x, y), steps = stack.pop()

        if x == d or y == d:
            if len(steps) < min_steps:
                min_steps = len(steps)
                result_steps = steps + [(x, y)]
            continue
        
        # Possible states
        possible_states = [
            (m, y, "Fill m"),                               # Fill m
            (x, n, "Fill n"),                               # Fill n
            (0, y, "Empty m"),                              # Empty m
            (x, 0, "Empty n"),                              # Empty n
            (x - min(x, n - y), y + min(x, n - y), "Pour m to n"),  # Pour m to n
            (x + min(y, m - x), y - min(y, m - x), "Pour n to m")   # Pour n to m
        ]

        for (new_x, new_y, action) in possible_states:
            if (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                stack.append(((new_x, new_y), steps + [(x, y, action)]))
    
    if result_steps is not None:
        print("Steps to measure {} liters:".format(d))
        for step in result_steps:
            print(step)
        return min_steps
    else:
        return -1

# Example usage
m = int(input('Enter the number for m: '))
n = int(input('Enter the number for n: '))
d = int(input('Enter the number for d: '))

result = min_operations(m, n, d)

if result != -1:
    print("Minimum number of operations:", result)
else:
    print("It's not possible to measure {} liters.".format(d))

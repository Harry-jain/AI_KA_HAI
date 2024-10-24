# BY BFS METHOD

from collections import deque

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def min_operations(m, n, d):
    # Check if it's possible to measure d liters
    if d > max(m, n) or d % gcd(m, n) != 0:
        return -1
    
    # BFS initialization
    queue = deque([((0, 0), [])])
    visited = set()
    visited.add((0, 0))

    while queue:
        (x, y), steps = queue.popleft()

        if x == d or y == d:
            steps.append((x, y))
            print("Steps to measure {} liters:".format(d))
            for step in steps:
                print(step)
            return len(steps) - 1
        
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
                queue.append(((new_x, new_y), steps + [(x, y, action)]))
    
    return -1

def main():
    print("Enter the capacities of the two jugs and the desired amount of water.")
    try:
        m = int(input("Capacity of the first jug (m): "))
        n = int(input("Capacity of the second jug (n): "))
        d = int(input("Desired amount of water (d): "))
        
        if m <= 0 or n <= 0 or d < 0:
            print("Capacities and desired amount must be positive integers.")
            return
        
        result = min_operations(m, n, d)
        
        if result != -1:
            print("Minimum number of operations:", result)
        else:
            print("It's not possible to measure {} liters.".format(d))
    
    except ValueError:
        print("Invalid input. Please enter integer values.")

if __name__ == "__main__":
    main()

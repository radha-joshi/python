from collections import deque


def water_jug_bfs(cap1, cap2, target):
    visited = set()
    queue = deque([(0, 0, 0)])

    print("BFS Example:")
    while queue:
        a, b, steps = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        print(f"Step {steps}: ({a}, {b})")

        if a == target or b == target:
            print(f"Reached target in {steps} steps.\n")
            return steps

        next_states = [
            (cap1, b),  # Fill jug 1
            (a, cap2),  # Fill jug 2
            (0, b),  # Empty jug 1
            (a, 0),  # Empty jug 2
            (a - min(a, cap2 - b), b + min(a, cap2 - b)),  # Pour 1 to 2
            (a + min(b, cap1 - a), b - min(b, cap1 - a))  # Pour 2 to 1
        ]

        for na, nb in next_states:
            if (na, nb) not in visited:
                queue.append((na, nb, steps + 1))

    print("Target cannot be reached.\n")
    return -1


def water_jug_dfs(cap1, cap2, target):
    visited = set()
    path = []

    def dfs(a, b, steps):
        if (a, b) in visited:
            return False

        visited.add((a, b))
        path.append((a, b))
        print(f"Step {steps}: ({a}, {b})")

        if a == target or b == target:
            print(f"Reached target in {steps} steps.\n")
            return True

        moves = [
            (cap1, b),
            (a, cap2),
            (0, b),
            (a, 0),
            (a - min(a, cap2 - b), b + min(a, cap2 - b)),
            (a + min(b, cap1 - a), b - min(b, cap1 - a))
        ]

        for na, nb in moves:
            if dfs(na, nb, steps + 1):
                return True

        # Backtrack if this path doesn't lead to the target
        path.pop()
        return False

    print("DFS Example:")
    if dfs(0, 0, 0):
        print("DFS Path:", path)
    else:
        print("Target cannot be reached.\n")


# Run the examples
water_jug_bfs(3, 5, 4)
water_jug_dfs(3, 5, 4)
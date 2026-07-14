from collections import deque

# Define the graph using an adjacency list
graph = {
    'Alice': ['Charlie', 'David'],
    'Bob': ['Emma', 'Fred'],
    'Charlie': ['Alice', 'Emma'],
    'David': ['Alice', 'Emma', 'Fred'],
    'Emma': ['Bob', 'Charlie', 'David'],
    'Fred': ['Bob', 'David']
}


def bfs(graph, start, goal):
    visited = set([start])
    queue = deque([[start]])  # Store the path instead of just nodes for easy extraction

    print("--- BFS Traversal Steps ---")
    step = 1

    while queue:
        path = queue.popleft()
        node = path[-1]

        print(f"Step {step}: Current Node = {node}, Path so far = {path}")
        step += 1

        if node == goal:
            return path

        # Sort alphabetically to maintain consistency with simulation
        for neighbor in sorted(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


def dfs(graph, start, goal):
    visited = set()
    stack = [[start]]  # Store the path instead of just nodes

    print("\n--- DFS Traversal Steps ---")
    step = 1

    while stack:
        path = stack.pop()
        node = path[-1]

        if node not in visited:
            visited.add(node)
            print(f"Step {step}: Current Node = {node}, Visited = {list(visited)}")
            step += 1

            if node == goal:
                return path

            # Push to stack in reverse-alphabetical order so alphabetical is popped first
            for neighbor in sorted(graph[node], reverse=True):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append(new_path)

    return None


# --- Execute Simulations ---
start_node = 'Alice'
goal_node = 'Bob'

bfs_path = bfs(graph, start_node, goal_node)
print(f"\n>> Final Path Found by BFS: {' -> '.join(bfs_path)}")

dfs_path = dfs(graph, start_node, goal_node)
print(f"\n>> Final Path Found by DFS: {' -> '.join(dfs_path)}")

def dfs(matrix, start_node):
    visited = []
    stack = [start_node]

    while stack:
        current = stack.pop()
        
        if current not in visited:
            visited.append(current)
            
            # Look for neighbors in reverse order so lower indices get popped first
            for neighbor in range(len(matrix) - 1, -1, -1):
                if matrix[current][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)
                    
    return visited
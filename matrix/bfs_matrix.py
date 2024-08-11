import collections


def bfs_matrix(matrix,start_row,start_col):
    n = len(matrix)
    visited = [[False for _ in range(n)] for _ in range(n) ]
    queue = collections.deque([(start_row,start_col)])
    visited[start_row][start_col] = True

    #define the four directions
    directions = [(0,-1),(0,1),(1,0),(-1,0)]

    while queue:
        curr_row, curr_col = queue.popleft()
        print(f"Visiting: ({curr_row}, {curr_col})")
        for d_row, d_col in directions:
            next_row, next_col = curr_row + d_row, curr_col + d_col

            if 0 <= next_row < n and 0 <= next_col < n and not visited[next_row][next_col]:
                queue.append((next_row,next_col))
                visited[next_row][next_col] = True

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
bfs_matrix(matrix, 0, 0)

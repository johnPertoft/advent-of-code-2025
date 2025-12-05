def remove_rolls(grid):
    total_removed = 0
    while True:
        grid, n_removed = remove_rolls_step(grid)
        total_removed += n_removed
        if n_removed == 0:
            break
    return total_removed

def remove_rolls_step(grid):
    max_r = len(grid)
    max_c = len(grid[0])
    to_remove = []
    for r in range(max_r):
        for c in range(max_c):
            if not grid[r][c]:
                continue

            n_neighboring_rolls = 0
            for nr, nc in get_neighbors(r, c, max_r, max_c):
                if grid[nr][nc]:
                    n_neighboring_rolls += 1
            if n_neighboring_rolls < 4:
                to_remove.append((r, c))
    
    n_removed = len(to_remove)
    for r, c in to_remove:
        grid[r][c] = False
    
    return grid, n_removed


def get_neighbors(r, c, max_r, max_c):
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            nr = r + dr
            nc = c + dc
            if dr == 0 and dc == 0:
                continue
            if nr < 0 or nr >= max_r:
                continue
            if nc < 0 or nc >= max_c:
                continue
            neighbors.append((nr, nc))
    return neighbors


with open("input-sample.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    grid = []
    for line in lines:
        row = [c == "@" for c in line]
        grid.append(row)
    
result = remove_rolls(grid)
print(result)
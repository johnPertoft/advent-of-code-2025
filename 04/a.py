def count_accessible_rolls_naive(grid):
    max_r = len(grid)
    max_c = len(grid[0])
    n_accessible_rolls = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if not grid[r][c]:
                continue

            n_neighboring_rolls = 0
            for nr, nc in get_neighbors(r, c, max_r, max_c):
                if grid[nr][nc]:
                    n_neighboring_rolls += 1
            if n_neighboring_rolls < 4:
                n_accessible_rolls += 1

    return n_accessible_rolls


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


with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    grid = []
    for line in lines:
        row = [c == "@" for c in line]
        grid.append(row)

result = count_accessible_rolls_naive(grid)
print(result)
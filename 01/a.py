def count_zeros(lines):
    dial = 50
    n_directions = 100
    n_zeros = 0
    for line in lines:
        direction = line[0]
        delta = int(line[1:])
        if direction == "L":
            delta = -delta
        dial = (dial + delta) % n_directions
        if dial == 0:
            n_zeros += 1
    return n_zeros


with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    result = count_zeros(lines)
    print(result)
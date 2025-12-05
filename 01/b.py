def count_zero_passes(lines):
    dial = 50
    n_directions = 100
    n_zero_passes = 0
    for line in lines:
        direction = line[0]
        delta = int(line[1:])
        
        # Count full rotations.
        full_rotations = delta // n_directions
        n_zero_passes += full_rotations
        delta = delta % n_directions

        if direction == "L":
            if dial != 0:
                if dial - delta <= 0:
                    n_zero_passes += 1
            dial = (dial - delta) % n_directions
        else:
            if dial != 0:
                if dial + delta >= n_directions:
                    n_zero_passes += 1
            dial = (dial + delta) % n_directions
    
    return n_zero_passes

with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    result = count_zero_passes(lines)
    print(result)
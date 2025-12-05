def check_freshness_naive(fresh_ranges, item_id):
    for start, end in fresh_ranges:
        if start <= item_id <= end:
            return True
    return False

with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    
    split_index = lines.index("")
    fresh_ranges_lines = lines[:split_index]
    available_ids_lines = lines[split_index + 1:]

    fresh_ranges = []
    for fresh_range in fresh_ranges_lines:
        start, end = map(int, fresh_range.split("-"))
        fresh_ranges.append((start, end))
    
    available_ids = [int(line) for line in available_ids_lines]

    n_fresh = 0
    for available_id in available_ids:
        if check_freshness_naive(fresh_ranges, available_id):
            n_fresh += 1
    
    print(n_fresh)

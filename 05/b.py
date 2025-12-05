def get_total_num_fresh_ids_naive(fresh_ranges):
    fresh_ids = set()
    for start, end in fresh_ranges:
        for item_id in range(start, end + 1):
            fresh_ids.add(item_id)
        print(len(fresh_ids))
    return len(fresh_ids)

def get_total_num_fresh_ids_2(fresh_ranges):
    fresh_ranges = sorted(fresh_ranges, key=lambda x: x[0])

    merged_ranges = []
    current_start, current_end = fresh_ranges[0]
    for start, end in fresh_ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            merged_ranges.append((current_start, current_end))
            current_start, current_end = start, end
    merged_ranges.append((current_start, current_end))

    total_fresh_ids = 0
    for start, end in merged_ranges:
        total_fresh_ids += end - start + 1
    
    return total_fresh_ids


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

    # Too slow
    #n_fresh = get_total_num_fresh_ids_naive(fresh_ranges)
    n_fresh = get_total_num_fresh_ids_2(fresh_ranges)
    print(n_fresh)
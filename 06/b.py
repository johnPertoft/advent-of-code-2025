def get_total_sum(lines):
    import math

    # Transpose input
    columns = list(map(list, zip(*lines)))

    i = 0
    total_sum = 0
    while True:
        op = columns[i][-1]
        
        # Find the next separator column
        for j in range(i + 1, len(columns)):
            if all(c == " " for c in columns[j]):
                break
        else:
            j = len(columns)
        
        # Get cephalopod numbers in this group
        ceph_numbers_str = ["".join(lc[:-1]).strip() for lc in columns[i:j]]
        ceph_numbers = [int(s) for s in ceph_numbers_str]
        
        if op == "*":
            result = math.prod(ceph_numbers)
        else:
            result = sum(ceph_numbers)
        
        total_sum += result
        
        i = j + 1
        if i >= len(columns):
            break
    
    return total_sum


with open("input.txt") as f:
    lines = f.readlines()
    result = get_total_sum(lines)
    print(result)
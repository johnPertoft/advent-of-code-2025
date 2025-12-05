def invalid_id(id):
    id_str = str(id)
    digits = [int(d) for d in id_str]

    # Can't be twice repeated with odd number of digits.
    if len(digits) % 2 == 1:
        return False

    mid = len(digits) // 2
    for i in range(mid):
        if digits[i] != digits[mid + i]:
            return False
    
    return True


with open("input.txt", "r") as f:
    data = f.read().strip()

    id_ranges = data.split(",")
    id_ranges = [r.strip().split("-") for r in id_ranges]
    id_ranges = [range(int(r[0]), int(r[1]) + 1) for r in id_ranges]

    invalid_id_sum = 0
    for r in id_ranges:
        for id in r:
            if invalid_id(id):
                invalid_id_sum += id
    
print(f"Sum of invalid IDs: {invalid_id_sum}")
from functools import lru_cache


# def get_largest_joltage(battery_bank: str) -> int:
#     return _get_largest_joltage(battery_bank)


# @lru_cache(maxsize=None)
# def _get_largest_joltage(battery_bank: str):
#     if len(battery_bank) <= 12:
#         joltage = int(battery_bank)
#         return joltage

#     largest_joltage = -1
#     for i in range(len(battery_bank)):
#         battery_bank_without_i = battery_bank[:i] + battery_bank[i+1:]
#         joltage = _get_largest_joltage(battery_bank_without_i)
#         if joltage > largest_joltage:
#             largest_joltage = joltage
    
#     return largest_joltage

# TODO: dp solution?

def get_largest_joltage(battery_bank: str) -> int:
    k = 12
    n = len(battery_bank)
    if n <= k:
        return int(battery_bank)
    
    remove = n - k
    stack = []
    for b in battery_bank:
        while stack and stack[-1] < b and remove > 0:
            stack.pop()
            remove -= 1
        stack.append(b)
    
    result_digits = stack[:k]
    return int(''.join(result_digits))


with open("input.txt") as f:
    lines = f.read().splitlines()
    lines = [line.strip() for line in lines]
    battery_banks = lines
    
    joltage_fn = get_largest_joltage
    sum_of_largest_joltage = 0
    for battery_bank in battery_banks:
        sum_of_largest_joltage += joltage_fn(battery_bank)
    
    print(sum_of_largest_joltage)

def get_largest_joltage(battery_bank):
    largest_joltage = -1
    for i in range(len(battery_bank) - 1):
        digit1 = battery_bank[i]
        for j in range(i + 1, len(battery_bank)):
            digit2 = battery_bank[j]
            joltage = int(str(digit1) + str(digit2))
            if joltage > largest_joltage:
                largest_joltage = joltage
    return largest_joltage


def get_largest_joltage2(battery_bank):
    largest_joltage = -1
    largest_first_digit = 1
    for i in range(len(battery_bank)):
        digit1 = battery_bank[i]
        if digit1 < largest_first_digit:
            continue
        for j in range(i + 1, len(battery_bank)):
            digit2 = battery_bank[j]
            joltage = int(str(digit1) + str(digit2))
            if joltage > largest_joltage:
                largest_joltage = joltage
                largest_first_digit = digit1
    return largest_joltage


with open("input.txt") as f:
    lines = f.read().splitlines()
    lines = [line.strip() for line in lines]
    battery_banks = []
    for line in lines:
        battery_banks.append([int(x) for x in line])
    
    import time
    for joltage_fn in [get_largest_joltage, get_largest_joltage2]:
        start_time = time.time()
        sum_of_largest_joltage = 0
        for battery_bank in battery_banks:
            sum_of_largest_joltage += joltage_fn(battery_bank)
        end_time = time.time()
        print(f"Using {joltage_fn.__name__}: {sum_of_largest_joltage} (took {end_time - start_time:.6f} seconds)")

    # sum_of_largest_joltage = 0
    # for battery_bank in battery_banks:
    #     sum_of_largest_joltage += get_largest_joltage2(battery_bank)
    # print(sum_of_largest_joltage)
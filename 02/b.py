from functools import lru_cache


@lru_cache
def get_divisors(n: int) -> list[int]:
    return [i for i in range(1, n) if n % i == 0]


def invalid_id(id):
    id_str = str(id)
    digits = [int(d) for d in id_str]

    divisors = get_divisors(len(digits))
    if not divisors:
        return False

    for d in divisors:
        if all(len(set(digits[i::d])) == 1 for i in range(d)):
            return True

    return False


def invalid_id2(id):
    id_str = str(id)
    digits = [int(d) for d in id_str]

    divisors = get_divisors(len(digits))
    if not divisors:
        return False

    for d in divisors:
        if all(digits[i] == digits[i + d] for i in range(len(digits) - d)):
            return True

    return False


def invalid_id3(id):
    id_str = str(id)
    digits = [int(d) for d in id_str]

    divisors = get_divisors(len(digits))
    if not divisors:
        return False

    for d in divisors:

        parts = []
        for i in range(0, len(digits), d):
            part = digits[i:i + d]
            parts.append(tuple(part))
        if len(set(parts)) == 1:
            return True

    return False


with open("input.txt", "r") as f:
    data = f.read().strip()

    id_ranges = data.split(",")
    id_ranges = [r.strip().split("-") for r in id_ranges]
    id_ranges = [range(int(r[0]), int(r[1]) + 1) for r in id_ranges]

    import time

    for invalid_id_func in [invalid_id, invalid_id2, invalid_id3]:
        t0 = time.perf_counter()

        invalid_id_sum = 0
        for r in id_ranges:
            for id in r:
                if invalid_id_func(id):
                    invalid_id_sum += id
        
        t1 = time.perf_counter()
        
        print(f"Sum of invalid IDs: {invalid_id_sum}")
        print(f"Time taken: {t1 - t0} seconds")
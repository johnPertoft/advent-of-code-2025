def get_total_sum(lines):
    operations = lines[-1]
    operations = operations.split()

    column_totals = []
    for operation in operations:
        column_totals.append(1 if operation == "*" else 0)

    for line in lines[:-1]:
        ns = [int(n.strip()) for n in line.split()]
        for i in range(len(ns)):
            if operations[i] == "*":
                column_totals[i] *= ns[i]
            else:
                column_totals[i] += ns[i]
        
    total_sum = sum(column_totals)
    return total_sum


def get_total_sum_short(lines):
    import math
    lines = [l.split() for l in lines]
    lines = list(map(list, zip(*lines)))
    return sum(sum(map(int, l[:-1])) if l[-1] == "+" else math.prod(map(int, l[:-1])) for l in lines)


with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    total_sum = get_total_sum(lines)
    print(total_sum)

    total_sum = get_total_sum_short(lines)
    print(total_sum)

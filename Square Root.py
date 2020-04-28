def get_indices(sequence):
    midpoint = (len(sequence) - 1) // 2
    return midpoint

def sqrt(x):
    sequence = range(x + 1)
    midpoint = get_indices(sequence)
    median = sequence[midpoint]
    while not pow(median, 2) <= x < pow(median + 1, 2):
        if pow(median, 2) > x:
            sequence = sequence[:midpoint]
            midpoint = get_indices(sequence)
        if pow(int(median), 2) < x:
            sequence = sequence[midpoint + 1:]
            midpoint = get_indices(sequence)
        median = sequence[midpoint]
    return median

if __name__ == "__main__":
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (2 == sqrt(8)) else "Fail")
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")
    print("Pass" if (31 == sqrt(1000)) else "Fail")
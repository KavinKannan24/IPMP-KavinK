def zero_sum_subarray(a):
    s, n_sum = set(), 0
    for x in a:
        n_sum += x
        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)
    return False

if __name__ == "__main__":
    a = list(map(int, input("Enter array elements: ").split()))
    if zero_sum_subarray(a):
        print("Subarray with 0 sum exists")
    else:
        print("No subarray with 0 sum exists")

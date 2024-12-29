def prod_except_self(arr):
    n = len(arr)
    if n == 1:
        return [1]

    l, r, p = [1] * n, [1] * n, [1] * n

    for i in range(1, n):
        l[i] = arr[i - 1] * l[i - 1]

    for j in range(n - 2, -1, -1):
        r[j] = arr[j + 1] * r[j + 1]

    for i in range(n):
        p[i] = l[i] * r[i]

    return p


arr = list(map(int, input("Enter array elements separated by space: ").split()))
res = prod_except_self(arr)
print(" ".join(map(str, res)))

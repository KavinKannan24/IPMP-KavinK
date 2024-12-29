def eq_point(arr):
    n = len(arr)
    if n == 1:
        return 1

    p, s = [0] * n, [0] * n
    p[0] = arr[0]
    for i in range(1, n):
        p[i] = p[i - 1] + arr[i]

    s[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        s[i] = s[i + 1] + arr[i]

    for i in range(n):
        if p[i] == s[i]:
            return i + 1

    return -1


arr = list(map(int, input("Enter array elements separated by space: ").split()))
print(eq_point(arr))

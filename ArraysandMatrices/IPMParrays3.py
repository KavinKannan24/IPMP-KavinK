def closest_three_sum(a, t):
    a.sort()
    c = float('inf')
    n = len(a)

    for i in range(n - 2):
        l, r = i + 1, n - 1

        while l < r:
            s = a[i] + a[l] + a[r]

            if abs(t - s) < abs(t - c):
                c = s

            if s < t:
                l += 1
            elif s > t:
                r -= 1
            else:
                return s

    return c

if __name__ == "__main__":
    a = list(map(int, input("Enter array elements: ").split()))
    t = int(input("Enter target sum: "))
    print(closest_three_sum(a, t))

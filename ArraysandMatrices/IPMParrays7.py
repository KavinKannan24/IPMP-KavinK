import sys

def closest_pair_sum(a):
    a.sort()
    n, res = len(a), sys.maxsize

    for i in range(n):
        x, l, r = a[i], i + 1, n - 1
        while l <= r:
            m = (l + r) // 2
            cur = a[m] + x

            if cur == 0:
                return 0

            if abs(cur) < abs(res):
                res = cur

            if cur < 0:
                l = m + 1
            else:
                r = m - 1

    return res

if __name__ == "__main__":
    a = list(map(int, input("Enter array elements: ").split()))
    print("Closest sum to 0:", closest_pair_sum(a))

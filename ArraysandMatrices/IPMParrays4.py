def four_sum(n, t):
    n.sort()
    res = []
    ln = len(n)

    for i in range(ln - 3):
        if i > 0 and n[i] == n[i - 1]:
            continue
        for j in range(i + 1, ln - 2):
            if j > i + 1 and n[j] == n[j - 1]:
                continue
            l, r = j + 1, ln - 1
            while l < r:
                s = n[i] + n[j] + n[l] + n[r]
                if s == t:
                    res.append([n[i], n[j], n[l], n[r]])
                    while l < r and n[l] == n[l + 1]:
                        l += 1
                    while l < r and n[r] == n[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < t:
                    l += 1
                else:
                    r -= 1
    return res

if __name__ == "__main__":
    n = list(map(int, input("Enter array elements: ").split()))
    t = int(input("Enter target sum: "))
    print(four_sum(n, t))

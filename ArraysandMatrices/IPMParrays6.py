def first_one(arr, l, h):
    res = -1
    while l <= h:
        m = l + (h - l) // 2
        if arr[m] == 1:
            res = m
            h = m - 1
        else:
            l = m + 1
    return res

def max_ones_row(mat):
    r, c = len(mat), len(mat[0])
    mx, res_row = -1, 0

    for i in range(r):
        idx = first_one(mat[i], 0, c - 1)
        if idx != -1 and c - idx > mx:
            mx = c - idx
            res_row = i

    return res_row

if __name__ == "__main__":
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))
    m = []
    print("Enter the matrix row by row:")
    for _ in range(r):
        m.append(list(map(int, input().split())))
    print("Row with max 1s:", max_ones_row(m))

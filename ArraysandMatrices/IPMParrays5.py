import sys

def find_triplet(arr):
    if len(arr) < 3:
        print("No triplet found")
        return

    s = 1
    mn = arr[0]
    mx = -sys.maxsize - 1
    sm = mn

    for i in range(1, len(arr)):
        if arr[i] == mn:
            continue
        elif arr[i] < mn:
            mn = arr[i]
            continue
        elif arr[i] < mx:
            mx = arr[i]
            sm = mn
        elif arr[i] > mx:
            if s == 1:
                sm = mn
            s += 1

            if s == 3:
                print(f"Triplet: {sm}, {mx}, {arr[i]}")
                return

            mx = arr[i]

    print("No triplet found")

if __name__ == "__main__":
    nums = list(map(int, input("Enter array elements: ").split()))
    find_triplet(nums)

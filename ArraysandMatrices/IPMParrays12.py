from random import randint

def shuffle(arr, n):
    for i in range(n - 1, 0, -1):
        j = randint(0, i + 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

# Take user input
arr = list(map(int, input("Enter array elements separated by space: ").split()))
n = len(arr)
print(shuffle(arr, n))

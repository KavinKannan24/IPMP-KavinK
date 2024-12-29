from collections import Counter

def sort_by_freq(arr):
    freq = Counter(arr)
    return sorted(arr, key=lambda x: (-freq[x], arr.index(x)))

# Take user input
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Sort and print the result
print(*sort_by_freq(arr))

def search_in_array(data, start, end, value):
    while start <= end:
        middle = start + (end - start) // 2

        if data[middle] == value:
            return True
        elif data[middle] < value:
            start = middle + 1
        else:
            end = middle - 1
    return False

def find_pair_with_sum(numbers, total):
    numbers.sort()

    for index in range(len(numbers)):
        diff = total - numbers[index]

        if search_in_array(numbers, index + 1, len(numbers) - 1, diff):
            return True

    return False

if __name__ == "__main__":
    data = [0, -1, 2, -3, 1]
    desired_sum = -2

    if find_pair_with_sum(data, desired_sum):
        print("true")
    else:
        print("false")

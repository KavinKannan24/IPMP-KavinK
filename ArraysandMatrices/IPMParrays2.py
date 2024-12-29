def locate_triplet_with_sum(data, target):
    length = len(data)

    for first in range(length - 2):
        for second in range(first + 1, length - 1):
            for third in range(second + 1, length):
                if data[first] + data[second] + data[third] == target:
                    print(f"Triplet is {data[first]}, {data[second]}, {data[third]}")
                    return True

    return False

if __name__ == "__main__":
    array = [1, 4, 45, 6, 10, 8]
    desired_sum = 22

    locate_triplet_with_sum(array, desired_sum)

import random
import cProfile


def randArr(length):
    arr = []
    for i in range(length):
        arr.append(random.randint(0, 1000))
    return arr


# Returns the index of the closest value to the target
def findClosesrt(arr, target):
    arr.sort()
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return arr[i]
        elif arr[i] > target:
            if i == 0:
                return arr[i]
            elif abs(arr[i] - target) < abs(arr[i - 1] - target):
                return arr[i]
            else:
                return arr[i - 1]
        i += 1
    return arr[i - 1]


if __name__ == '__main__':
    arr = randArr(1000)
    print(arr)
    arr.sort()
    print(arr)
    print(findClosesrt(arr, 500))

    cProfile.run('findClosesrt(arr, 500)')
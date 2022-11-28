import cProfile


def findMode(arr):
    arr.sort()  # Array must be sorted before we apply the algorithm.
    i = 0
    mode_frequency = 0
    while i < len(arr):
        run_length = 1
        run_value = arr[i]
        while i + run_length < len(arr) and arr[i + run_length] == run_value:
            run_length += 1
        if run_length > mode_frequency:
            mode_frequency = run_length
            mode_value = run_value
        i += run_length
    return mode_value


arr = [5, 1, 5, 6, 5, 5, 7]
print(findMode(arr))  # Output: 5

arr = [5, 1, 5, 6, 5, 5, 7]
arr.sort()
print(arr)
print(findMode(arr))  # Output: 5

cProfile.run('findMode(arr)')
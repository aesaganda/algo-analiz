# Time Complexity: O(N + K)
# Space Complexity: O(K)
# Worst Case: Aralık büyükse ve sayıların dağılımı düzensizse
# Best Case: Bütün elemanlar aynı olursa
# Average Case: O(N+K) (N ve K eşit etki eder)

import random

# Generate a dataset of 1000 random numbers between 0 and 5000
numbers = [random.randint(0, 5000) for _ in range(1000)]

print("Unsorted:", numbers)

# Create a counting array of size 5001 (since the maximum value of the numbers in the dataset is 5000)
counts = [0] * 5001

# Count the number of occurrences of each number in the dataset in the counting array
for num in numbers:
    counts[num] += 1

# Sort the counting array in ascending order
counts = [count for count in counts if count > 0]

# Use the sorted counting array to sort the original dataset in ascending order
sorted_numbers = []
for num, count in enumerate(counts):
    for _ in range(count):
        sorted_numbers.append(num)

# Print the sorted dataset
print("Sorted:", sorted_numbers)

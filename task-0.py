import random

print("\n\nA list of 30 random numbers from -100 to +100:")
array = range(-100, 100)
numbers = random.sample(array, 30)
print(numbers)

print("\nMaximum item list:")
print(max(numbers))

print("\nSequence number of the maximum item list:")
print(numbers.index(max(numbers)))

print("\nPairs of negative numbers standing side by side:\n")
for i in range(len(numbers)-1):
    if numbers[i] < 0 and numbers[i+1] < 0:
        print(numbers[i], numbers[i+1])

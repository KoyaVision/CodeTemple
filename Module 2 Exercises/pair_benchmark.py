import time

def count_pairs_slow(numbers, target):
    count = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                count += 1

    return count

def count_pairs_fast(numbers, target):
    count = 0
    seen = set()

    for number in numbers:
        needed = target - number

        if needed in seen:
            count += 1

        seen.add(number)

    return count

numbers = [1, 2, 3, 4, 5]
target = 6

print(count_pairs_slow(numbers, target))
print(count_pairs_fast(numbers, target))

sizes = [1000, 5000, 10000]

for size in sizes:
    numbers = list(range(size))
    target = size - 1

    start = time.perf_counter()
    slow_result = count_pairs_slow(numbers, target)
    slow_time = time.perf_counter() - start

    start = time.perf_counter()
    fast_result = count_pairs_fast(numbers, target)
    fast_time = time.perf_counter() - start

    print("List size:", size)
    print("Slow result:", slow_result)
    print("Slow time:", slow_time)
    print("Fast result:", fast_result)
    print("Fast time:", fast_time)
    print()

# Benchmark Output

# Small test
# Slow result: 2
# Fast result: 2
#
# List size: 1000
# Slow result: 500
# Slow time: 0.025409666999999997
# Fast result: 500
# Fast time: 8.770899999999832e-05

# List size: 5000
# Slow result: 2500
# Slow time: 0.7006770830000001
# Fast result: 2500
# Fast time: 0.0005107920000000377

# List size: 10000
# Slow result: 5000
# Slow time: 2.6194525410000002
# Fast result: 5000
# Fast time: 0.0008483749999999013
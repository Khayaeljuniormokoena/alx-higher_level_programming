#!/usr/bin/python3

def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        # Check if mid is a peak
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    # 'low' now points to the peak
    return list_of_integers[low]

# Test cases
print(find_peak([1, 2, 4, 6, 3]))    # Output: 6
print(find_peak([4, 2, 1, 2, 3, 1])) # Output: 3
print(find_peak([2, 2, 2]))          # Output: 2
print(find_peak([]))                 # Output: None
print(find_peak([-2, -4, 2, 1]))     # Output: 2
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))  # Output: 4

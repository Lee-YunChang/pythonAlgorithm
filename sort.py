import random
import time

array = random.sample(range(1, 1000), 100)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

sort_functions = [bubble_sort, selection_sort, insertion_sort]
sort_times = {}

for sort_function in sort_functions:
    arr_copy = array[:]
    start_time = time.time()
    sort_function(arr_copy)
    end_time = time.time()
    sort_times[sort_function.__name__] = end_time - start_time

print(sort_times)

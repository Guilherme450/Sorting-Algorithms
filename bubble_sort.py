# Bubble sort algorithm.
# The time complexity of bubble sort algorithm is O(n^2).

def bubble_sort(array):
    '''The bubble_sort function takes an unsorted array and returns it sorted.
    args:
        array(list): An unsorted array.

    returns:
        (list): A sorted array.
    '''
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

array = [6,8,7,2,9,1,10,3]
print(bubble_sort(array))
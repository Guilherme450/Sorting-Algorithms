# Insertion sort algorithm.
# The time complexity of insertion sort is O(n^2) for both worst and best cases.

# Creating the swap helper function.
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def insertion_sort(array):
    '''The insertion_sort function returns a sorted array.
    args:
        array(list): An unsorted array.

    returns:
        (list): A sorted array.
    '''
    n = len(array)
    for i in range(1, n):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j - 1, j)
            j -= 1
    return array

array = [6,10,2,1,9,7,3,8]
print(insertion_sort(array))
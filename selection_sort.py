# Selection sort algorithm.
# Time complexity: O(n^2).
# This sort of algorithm selects a minimum number and put it on a correct index.

def selection_sort(array):
    '''selection sort algorithm for sorting an array.
    arg:
        array(list): An unsorted list of numbers.

    returns:
        (list): A sorted list of numbers.
    '''
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            # Verify if the element on the min_index is more bigger than the element on the j index.
            if array[min_index] > array[j]:
                min_index = j
        # Changing the place of the elements.
        array[i], array[min_index] = array[min_index], array[i]
    return array

array = [7,3,8,9,10,6,2,1]
print(selection_sort(array))
import random

def qsort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]

        for num in array:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            elif num > pivot:
                greater.append(num)
        return qsort(less) + equal + qsort(greater)

    else:
        return array

print(qsort([random.randrange(1, 500, 1) for i in range(1000)]))

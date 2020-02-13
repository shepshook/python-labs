import argparse
import sys

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a


def merge_sort(array):
    n = len(array)
    if n > 1:
        mid = n // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


def quick_sort(array):
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
        return quick_sort(less) + equal + quick_sort(greater)

    else:
        return array


def word_counter(text):
    words = text.split()
    dic = {}
    for word in words:
        if dic.get(word) is None:
            dic[word] = 1
        else:
            dic[word] += 1

    sorted_words = [k for k, _ in sorted(dic.items(), key=lambda item: item[1], reverse=True)]

    for i in range(min(len(sorted_words), 10)):
        print(sorted_words[i], end=" ")
    print("\n")    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Specify a file to load data from")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--counter", action="store_true", help="Prints 10 most used words of the text")
    group.add_argument("--qsort", action="store_true", help="Sorts an array from a file with Quick Sort")
    group.add_argument("--mergesort", action="store_true", help="Sorts an array from f file with Merge Sort")
    group.add_argument("--fib", type=int, help="Prints some Fibonacci numbers")

    args = parser.parse_args()

    if args.counter:
        if args.file:
            with open(args.file) as f:
                word_counter(f.read())
        else:
            print("Input text", end="\n")
            text = input()
            word_counter(text)

    elif args.qsort:
        if args.file:
            with open(args.file) as f:
                array = [int(x) for x in f.read().split()]
                print(quick_sort(array))
        else:
            print("File is not specified")

    elif args.mergesort:
        if args.file:
            with open(args.file) as f:
                array = [int(x) for x in f.read().split()]
                merge_sort(array)
                print(array)
        else:
            print("File is not specified")

    elif args.fib:
        for num in fib(args.fib):
            print(num, end="\n")


def swap(A, lo, hi):
    A[lo],A[hi] = A[hi],A[lo]

def partition(A, lo, hi):
    pivot = A[hi]
    i = lo
    for j in range(i,hi):  # [11,9,29,7,2,15,28]
        if A[j]<pivot:
            swap(A, i, j)
            i += 1
    swap(A,i,hi)
    return i

def  quicksort(A, lo, hi):
    if lo<hi:
        p=partition(A, lo, hi)
        quicksort(A, lo, p-1)
        quicksort(A, lo+1,hi)
    

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    new_var = quicksort(elements, 0, len(elements)-1)
    print(elements)

    # tests = [
    #     [11,9,29,7,2,15,28],
    #     [3, 7, 9, 11],
    #     [25, 22, 21, 10],
    #     [29, 15, 28],
    #     [],
    #     [6]
    # ]

    # for elements in tests:
    #     quicksort(elements, 0, len(elements)-1)
    #     print(f'sorted array: {elements}')

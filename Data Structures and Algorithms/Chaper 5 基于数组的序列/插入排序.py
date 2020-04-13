def insertion_sort(A):
    """ Sort list of comparable elements into nondecreasing order. """
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur


if __name__ == "__main__":
    A = [1, 5, 6, 4, 7, 3, 8, 5, 2, 8]
    insertion_sort(A)
    print(A)

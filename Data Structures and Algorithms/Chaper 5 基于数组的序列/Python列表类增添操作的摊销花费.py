from time import time


def comptuter_average(n):
    """ Perform n appends to an empty list and return average time elaosed. """
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end-start)/n


if __name__ == "__main__":
    print(comptuter_average(100))
    print(comptuter_average(1000))
    print(comptuter_average(10000))
    print(comptuter_average(100000))
    print(comptuter_average(1000000))
    print(comptuter_average(10000000))

    



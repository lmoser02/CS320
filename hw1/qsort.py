# quicksort a list
# (See hw1.pdf for requirements.)

def quicksort(alist):
    # +++your code here+++
    def qsort(thelist, low, high):
        if low < high:
            part = partition(thelist, low, high)
            qsort(thelist, low, part)
            qsort(thelist, part + 1, high)

    def partition(thelist, low, high):
        pivot = thelist[low]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            j -= 1
            while(thelist[i] < pivot):
                i += 1
            while(thelist[j] > pivot):
                j -= 1

            if i >= j:
                return j

            thelist[i], thelist[j] = thelist[j], thelist[i]
      #the swap
    qsort(alist, 0, len(alist)-1)

if __name__ == "__main__":
    a = [1,3,5,2,9,6,7,5]
    b = [42]       # special singleton case
    c = []         # special empty list case
    quicksort(a)
    quicksort(b)
    quicksort(c)
    print(a)       # => [1,2,3,5,5,6,7,9]
    print(b)       # => [42]
    print(c)       # => []

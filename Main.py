import random
import time
import xlwt
from xlwt import Workbook


def randomArray(arr, length):
    for x in range(0, length):
        arr.append(random.randint(1, 100000))


def listPrinter(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swapping values if j is bigger than i
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def mergeSort(arr):
    if len(arr) > 1:
        # find middle
        mid = len(arr) // 2
        # dividing the elements
        L = arr[:mid]
        # dividing into two halves
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def insertionSort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > current:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = current


def heapify(arr, size, i):
    largest = i  # root
    L = 2 * i + 1  # Left
    R = 2 * i + 2  # Right

    # Left Child and root check
    if L < size and arr[i] < arr[L]:
        largest = L
    # Right Child and root check
    if R < size and arr[largest] < arr[R]:
        largest = R

    # Root Canal
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Run it back
        heapify(arr, size, largest)


def heapSort(arr):
    size = len(arr)
    # Build
    for i in range(size, -1, -1):
        heapify(arr, size, i)

    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


def partition(arr, low, high):
    i = (low - 1)
    piv = arr[high]
    for j in range(low, high):

        if arr[j] <= piv:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

    # The main function that implements QuickSort


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def countingSort(array, spot):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // spot
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // spot
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, size):
        array[i] = output[i]


def radixSort(array):
    if len(array) != 0:
        max_element = max(array)
        place = 1
        while max_element // place > 0:
            countingSort(array, place)
            place *= 10


def cocktailSort(array):
    for i in range(len(array) // 2):
        swap = False
        for j in range(1 + i, len(array) - i):
            if array[j] < array[j - 1]:
                # Swapping places
                array[j], array[j - 1] = array[j - 1], array[j]
                swap = True
        if not swap:
            break
        swap = False
        for j in range(len(array) - i - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                swap = True
        if not swap:
            break


wb = Workbook()
# Setup For Excel
sheet1 = wb.add_sheet('sheet1')
sheet1.write(1, 0, 'Bubble Sort')
sheet1.write(2, 0, 'Merge Sort')
sheet1.write(3, 0, 'Insertion Sort')
sheet1.write(4, 0, 'Heap Sort')
sheet1.write(5, 0, 'Quick Sort')
sheet1.write(6, 0, 'Radix Sort')
sheet1.write(7, 0, 'Cocktail Sort')

for i in range(1, 11):
    arr1 = []
    randomArray(arr1, i * 100000)
    arr2 = []
    randomArray(arr2, i * 100000)
    arr3 = []
    randomArray(arr3, i * 100000)
    arr4 = []
    randomArray(arr4, i * 100000)
    arr5 = []
    randomArray(arr5, i * 100000)
    arr6 = []
    randomArray(arr6, i * 100000)
    arr7 = []
    randomArray(arr7, i * 100000)

    print(i * 100000)
    # BubbleSort
 #   start1 = time.time()
  #  bubbleSort(arr1)
  #  end1 = time.time()
  #  print("Bubble Sort Time: ")
  #  BSTime = end1 - start1
  #  print(BSTime)
  #  listPrinter(arr1)

    # Merge sort
  #  start2 = time.time()
    ##mergeSort(arr2)
    #end2 = time.time()
    #print("Merge Sort time:")
    #MSTime = end2 - start2
    #print(MSTime)
   # listPrinter(arr2)

    # Insertion Sort
    #start3 = time.time()
    #insertionSort(arr3)
    #end3 = time.time()
    #print("Insertion Sort time:")
    #ISTime = end3 - start3
    #print(ISTime)
   # listPrinter(arr3)

    # Heap Sort
    #start4 = time.time()
    #heapSort(arr4)
    #end4 = time.time()
    #print("Heap Sort time:")
    #HSTime = end4 - start4
    #print(HSTime)
    #listPrinter(arr4)

    # Quick Sort
    n = len(arr5)
    start5 = time.time()
    quickSort(arr5, 0, n - 1)
    end5 = time.time()
    print("Quick Sort time:")
    QSTime = end5 - start5
    print(QSTime)
 #   listPrinter(arr5)

    # Radix Sort
    start6 = time.time()
    radixSort(arr6)
    end6 = time.time()
    print("Radix Sort time:")
    RSTime = end6 - start6
    print(RSTime)
  #  listPrinter(arr6)

    # Cocktail Sort
    #start7 = time.time()
    #cocktailSort(arr7)
    #end7 = time.time()
    #print("Cocktail Sort time:")
    #CSTime = end7 - start7
    #print(CSTime)
    #listPrinter(arr7)

    # Printing Values to an Excel spreadsheet
    sheet1.write(0, i, i * 1000)

    # Bubble Sort
    #sheet1.write(1, i, BSTime)

    # Merge Sort
#    sheet1.write(2, i, MSTime)

    # Insertion Sort
   # sheet1.write(3, i, ISTime)

    # Heap Sort
 #00   sheet1.write(4, i, HSTime)

    # Quick Sort
    sheet1.write(5, i, QSTime)

    # Radix Sort
    sheet1.write(6, i, RSTime)

    # Cocktail Sort
 #   sheet1.write(7, i, CSTime)

wb.save('DSASortingValues.xls')

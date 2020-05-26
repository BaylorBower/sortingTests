import unittest
from Main import bubbleSort
from Main import mergeSort
from Main import heapSort
from Main import insertionSort
from Main import radixSort
from Main import quickSort
from Main import cocktailSort

# Format
# class MyTestCase(unittest.TestCase):
#    def test_something(self):
#        self.assertEqual(True, False)


class TestBubbleSort(unittest.TestCase):
    def test_EmptyList(self):
        lst = []
        sortedList = lst
        bubbleSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_SingleList(self):
        lst = [1]
        sortedList = lst
        bubbleSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_TwoSorted(self):
        lst = [1, 2]
        sortedList = lst
        bubbleSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_TwoUnsorted(self):
        lst = [2, 1]
        sortedList = lst
        bubbleSort(sortedList)
        self.assertEqual(sortedList, [1, 2])

    def test_WithZero(self):
        lst = [10, 0]
        sortedList = lst
        bubbleSort(sortedList)
        self.assertEqual(sortedList, [0, 10])

    def test_WithDuplicate(self):
        lst = [1, 2, 2, 1, 0, 0, 15, 15]
        sortedList = lst
        bubbleSort(sortedList)
        self.assertEqual(sortedList, [0, 0, 1, 1, 2, 2, 15, 15])

    def test_BigNumbers(self):
        lst = [135604, 1000000, 45, 78435, 456219832, 2, 546]
        sortedList = lst
        bubbleSort(sortedList)
        self.assertEqual(sortedList,
                         [2, 45, 546, 78435, 135604, 1000000, 456219832])


class TestMergeSort(unittest.TestCase):
    def test_EmptyList(self):
        lst = []
        sortedList = lst
        mergeSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_SingleList(self):
        lst = [1]
        sortedList = lst
        mergeSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_TwoSorted(self):
        lst = [1, 2]
        sortedList = lst
        mergeSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_TwoUnsorted(self):
        lst = [2, 1]
        sortedList = lst
        mergeSort(sortedList)
        self.assertEqual(sortedList, [1, 2])

    def test_WithZero(self):
        lst = [10, 0]
        sortedList = lst
        mergeSort(sortedList)
        self.assertEqual(sortedList, [0, 10])

    def test_WithDuplicate(self):
        lst = [1, 2, 2, 1, 0, 0, 15, 15]
        sortedList = lst
        mergeSort(sortedList)
        self.assertEqual(sortedList, [0, 0, 1, 1, 2, 2, 15, 15])

    def test_BigNumbers(self):
        lst = [135604, 1000000, 45, 78435, 456219832, 2, 546]
        sortedList = lst
        mergeSort(sortedList)
        self.assertEqual(sortedList,
                         [2, 45, 546, 78435, 135604, 1000000, 456219832])


class TestInsertionSort(unittest.TestCase):
    def test_EmptyList(self):
        lst = []
        sortedList = lst
        insertionSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_SingleList(self):
        lst = [1]
        sortedList = lst
        insertionSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_TwoSorted(self):
        lst = [1, 2]
        sortedList = lst
        insertionSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_TwoUnsorted(self):
        lst = [2, 1]
        sortedList = lst
        insertionSort(sortedList)
        self.assertEqual(sortedList, [1, 2])

    def test_WithZero(self):
        lst = [10, 0]
        sortedList = lst
        insertionSort(sortedList)
        self.assertEqual(sortedList, [0, 10])

    def test_WithDuplicate(self):
        lst = [1, 2, 2, 1, 0, 0, 15, 15]
        sortedList = lst
        insertionSort(sortedList)
        self.assertEqual(sortedList, [0, 0, 1, 1, 2, 2, 15, 15])

    def test_BigNumbers(self):
        lst = [135604, 1000000, 45, 78435, 456219832, 2, 546]
        sortedList = lst
        insertionSort(sortedList)
        self.assertEqual(sortedList,
                         [2, 45, 546, 78435, 135604, 1000000, 456219832])


class TestHeapSort(unittest.TestCase):
    def test_EmptyList(self):
        lst = []
        sortedList = lst
        heapSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_SingleList(self):
        lst = [1]
        sortedList = lst
        heapSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_TwoSorted(self):
        lst = [1, 2]
        sortedList = lst
        heapSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_TwoUnsorted(self):
        lst = [2, 1]
        sortedList = lst
        heapSort(sortedList)
        self.assertEqual(sortedList, [1, 2])

    def test_WithZero(self):
        lst = [10, 0]
        sortedList = lst
        heapSort(sortedList)
        self.assertEqual(sortedList, [0, 10])

    def test_WithDuplicate(self):
        lst = [1, 2, 2, 1, 0, 0, 15, 15]
        sortedList = lst
        heapSort(sortedList)
        self.assertEqual(sortedList, [0, 0, 1, 1, 2, 2, 15, 15])

    def test_BigNumbers(self):
        lst = [135604, 1000000, 45, 78435, 456219832, 2, 546]
        sortedList = lst
        heapSort(sortedList)
        self.assertEqual(sortedList,
                         [2, 45, 546, 78435, 135604, 1000000, 456219832])


class TestRadixSort(unittest.TestCase):
    def test_EmptyList(self):
        lst = []
        sortedList = lst
        radixSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_SingleList(self):
        lst = [1]
        sortedList = lst
        radixSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_TwoSorted(self):
        lst = [1, 2]
        sortedList = lst
        radixSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_TwoUnsorted(self):
        lst = [2, 1]
        sortedList = lst
        radixSort(sortedList)
        self.assertEqual(sortedList, [1, 2])

    def test_WithZero(self):
        lst = [10, 0]
        sortedList = lst
        radixSort(sortedList)
        self.assertEqual(sortedList, [0, 10])

    def test_WithDuplicate(self):
        lst = [1, 2, 2, 1, 0, 0, 15, 15]
        sortedList = lst
        radixSort(sortedList)
        self.assertEqual(sortedList, [0, 0, 1, 1, 2, 2, 15, 15])

    def test_BigNumbers(self):
        lst = [135604, 1000000, 45, 78435, 456219832, 2, 546]
        sortedList = lst
        radixSort(sortedList)
        self.assertEqual(sortedList,
                         [2, 45, 546, 78435, 135604, 1000000, 456219832])


class TestQuickSort(unittest.TestCase):
    def test_EmptyList(self):
        lst = []
        sortedList = lst
        quickSort(sortedList, 0, len(lst)-1)
        self.assertEqual(lst, sortedList)

    def test_SingleList(self):
        lst = [1]
        sortedList = lst
        quickSort(sortedList, 0, len(lst)-1)
        self.assertEqual(lst, sortedList)

    def test_TwoSorted(self):
        lst = [1, 2]
        sortedList = lst
        quickSort(sortedList, 0, len(lst)-1)
        self.assertEqual(lst, sortedList)

    def test_TwoUnsorted(self):
        lst = [2, 1]
        sortedList = lst
        quickSort(sortedList, 0, len(lst)-1)
        self.assertEqual(sortedList, [1, 2])

    def test_WithZero(self):
        lst = [10, 0]
        sortedList = lst
        quickSort(sortedList, 0, len(lst)-1)
        self.assertEqual(sortedList, [0, 10])

    def test_WithDuplicate(self):
        lst = [1, 2, 2, 1, 0, 0, 15, 15]
        sortedList = lst
        quickSort(sortedList, 0, len(lst)-1)
        self.assertEqual(sortedList, [0, 0, 1, 1, 2, 2, 15, 15])

    def test_BigNumbers(self):
        lst = [135604, 1000000, 45, 78435, 456219832, 2, 546]
        sortedList = lst
        quickSort(sortedList, 0, len(lst)-1)
        self.assertEqual(sortedList,
                         [2, 45, 546, 78435, 135604, 1000000, 456219832])


class TestCocktailSort(unittest.TestCase):
    def test_EmptyList(self):
        lst = []
        sortedList = lst
        cocktailSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_SingleList(self):
        lst = [1]
        sortedList = lst
        cocktailSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_TwoSorted(self):
        lst = [1, 2]
        sortedList = lst
        cocktailSort(sortedList)
        self.assertEqual(lst, sortedList)

    def test_TwoUnsorted(self):
        lst = [2, 1]
        sortedList = lst
        cocktailSort(sortedList)
        self.assertEqual(sortedList, [1, 2])

    def test_WithZero(self):
        lst = [10, 0]
        sortedList = lst
        cocktailSort(sortedList)
        self.assertEqual(sortedList, [0, 10])

    def test_WithDuplicate(self):
        lst = [1, 2, 2, 1, 0, 0, 15, 15]
        sortedList = lst
        cocktailSort(sortedList)
        self.assertEqual(sortedList, [0, 0, 1, 1, 2, 2, 15, 15])

    def test_BigNumbers(self):
        lst = [135604, 1000000, 45, 78435, 456219832, 2, 546]
        sortedList = lst
        cocktailSort(sortedList)
        self.assertEqual(sortedList,
                         [2, 45, 546, 78435, 135604, 1000000, 456219832])


if __name__ == '__main__':
    unittest.main()

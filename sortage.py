list1 = [10, 20, 30, 40, 51, 55, 20, 32, 521, 45, 84, 54, 65, 625]
list2 = [10, 20, 30, 40, 51, 55, 20, 32, 521, 45, 84, 54, 65, 740]


# bubble sort
def bubble_sort(lister):
    for i in range(len(lister) - 1):
        for j in range(len(lister) - i - 1):
            if lister[j] > lister[j + 1]:
                lister[j], lister[j + 1] = lister[j + 1], lister[j]


# selection sort
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


# to print top 5 scores from list
def top5(iterable):
    print("Top 5 scores are :")
    for i in range(1, 6):
        print(iterable[0 - i], end=" ")
    print()


bubble_sort(list1)
selection_sort(list2)
top5(list1)
top5(list2)


Top 5 scores are :
625 521 84 65 55
Top 5 scores are :
740 521 84 65 55

array = [64, 25, 12, 22, 11, 22]
for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
print(array[len(array)-5:len(array)])

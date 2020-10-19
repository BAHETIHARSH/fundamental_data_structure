list1=[131, 601, 306, 233, 643, 306, 322, 999, 367, 755, 226, 814, 148, 797, 918, 104, 598, 439, 437, 685]

for i in range(len(list1)):
    temp=list1[i]
    j = i - 1                     
    while j>=0 and temp<list1[j]:
            list1[j+1]=list1[j]
            j -= 1

    list1[j+1] = temp
    print(list1, i)


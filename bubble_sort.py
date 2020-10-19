list=[10,20,30,40,51,55,20,32,521,45,84,54,65]
for i in range(len(list)-1):
    for j in range(len(list)-i-1):
        if list[j]>list[j+1]:
            list[j],list[j + 1]=list[j+1],list[j]
print(list)

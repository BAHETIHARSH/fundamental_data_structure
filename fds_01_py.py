# students playing cricket
group_a = ['Rahul', 'Kapil', 'Sarang', 'Sachin', 'Nikhil']
# students playing badminton
group_b = ['Rahul', 'Sagar', 'Sarang', 'Abhi', 'Amol']
# students playing football
group_c = ['Rahul', 'Kapil', 'Sarang', 'Abhi', 'Varad']


# Number of students who play neither cricket nor badminton : 1
# List of students who play either cricket or badminton but not both :
# ['Kapil', 'Sachin', 'Nikhil', 'Sagar', 'Abhi', 'Amol']
# List of students who play both cricket and badminton :
# ['Rahul', 'Sarang']
# Number of students who play cricket and football but not badminton : 1


def crick_or_bat_not_both(list1, list2):
    list3 = list1 + list2
    for i in list1:
        if i in list2:
            list3.remove(i)
            list3.remove(i)
    return list3


print("List of students who play either cricket or badminton but not both :")
print(crick_or_bat_not_both(group_a, group_b))


# List of students who play both cricket and badminton :
def union(list1, list2):
    list_return = []
    for i in list1:
        if i in list2:
            list_return.append(i)
    return list_return


print("List of students who play both cricket and badminton :")
print(union(group_a, group_b))


# Number of students who play neither cricket nor badminton


def neither_cric_nor_bad(list1, list2, list3):
    list_return = list3
    for i in list3:
        if i in list1 or i in list2:
            list_return.remove(i)
    return len(list_return)


print("Number of students who play neither cricket nor badminton : ", neither_cric_nor_bad(group_a, group_b, group_c))


# Number of students who play cricket and football but not badminton : 1
def crick_and_fotball_not_badmination(list_a, list_b, list_c):
    list_return = []
    for i in list_a:
        if i in list_c:
            if i not in list_b:
                list_return.append(i)
    return len(list_return)


print("Number of students who play cricket and football but not badminton : ",
      crick_and_fotball_not_badmination(group_a, group_b, group_c))

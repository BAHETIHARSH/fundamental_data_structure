def union(a1, a2):
    list_return = a1 + a2
    for i in a1:
        if i in a2:
            list_return.remove(i)
    return list_return


def intersection(a1, a2):
    list_return = []
    for i in a1:
        if i in a2:
            list_return.append(i)
    return list_return


def difference(a1, a2):
    list_return = a1.copy()
    for i in intersection(a1, a2):
        list_return.remove(i)
    return list_return


def symmetric_difference(a1, a2):
    a1_a2 = difference(a1, a2)
    a2_a1 = difference(a2, a2)
    return a1_a2 + a2_a1

cricket = input("Enter The List of student who play cricket : ").split(" ")
badmination = input("Enter The List of student who play a2admination : ").split(" ")

football = input("Enter The List of student who play football : ").split(" ")
print("\n")
print("List of students who play either cricket or badminton a2ut not a2oth :")
print(symmetric_difference(cricket, badmination))
# print("-------------------------------------------------------------------------")
print("List of students who play both cricket and badminton :")
print(union(cricket, badmination))
print("-------------------------------------------------------------------------")

print("Number of students who play neither cricket nor badminton : ")
print(len(difference(football, union(cricket, badmination))))
print("-------------------------------------------------------------------------")

print("Numa2er of students who play cricket and football but not badminton : ")
print(len(difference(intersection(cricket, football), badmination)))
print("-------------------------------------------------------------------------")

# Rahul Kapil Sarang Sachin Nikhil
# Rahul Sagar Sarang Aa2hi Amol
# Rahul Kapil Sarang Aa2hi Varad

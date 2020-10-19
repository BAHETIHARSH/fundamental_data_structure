list = [90, 99, 98, 95, 94, 0, 0, 0, 0, 0, 45, 78, 98, 45, 56, 13, 98, 72, 65, 84, 48, 45, 94, 95, 96, 97, 99,90,90]


def list_to_dict(input_list):
    dictionary = {}
    for i in input_list:
        dictionary[i] = dictionary.get(i, 0) + 1
    return dictionary


def mean(input_list):
    add = 0
    for i in input_list:
        add += i
    return add / len(input_list)


def minimum(input_list):
    lower = input_list[0]
    for i in input_list:
        if i == 0:
            continue
        else:
            if lower > i:
                lower = i
    return lower


def maximum(input_list):
    higher = 0
    for i in input_list:
        if i == 0:
            continue
        else:
            if higher < i:
                higher = i
    return higher


def max_frequency(di):
    max = 0
    for i in di:
        if i == 0:
            continue
        elif di[i] > max:
            max = i
    return max


# The average score of class
print("The average score of class : ", mean(list))

# Highest score and lowest score of class
print("Highest score of class : ", maximum(list))
print("lowest score of class : ", minimum(list))

# Count of students who were absent for the test
dict = list_to_dict(list)
print("Count of students who were absent for the test : ", dict[0])

# Display mark with highest frequency
frequency = list_to_dict(list)
p = max_frequency(frequency)
print("Mark's with highest frequency is {} and its frequency is {} ".format(p,frequency[p]))


# The average score of class :  64.96551724137932
# Highest score of class :  99
# lowest score of class :  13
# Count of students who were absent for the test :  5
# Mark's with highest frequency is 90 and its frequency is 3

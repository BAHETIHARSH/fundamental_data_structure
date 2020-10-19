# a) To display word with the longest length
def longtest_word(input_string):
    longest = ""
    for i in input_string.split():
        if len(longest) < len(i):
            longest = i
    return longest


# b) To determines the frequency of occurrence of particular character in the string
def frequency_chr(input_string):
    dictionary = {}

    for i in input_string:
        dictionary[i] = dictionary.get(i, 0) + 1
    return dictionary


# c) To check whether given string is palindrome or not
def palindrome(input_string):
    for i in range(0, len(input_string) // 2 + 1):
        if input_string[i] == input_string[len(input_string) - i - 1]:
            continue
        else:
            return "not a palindrome"
    return ' a palindrome'


# d) To display index of first appearance of the substring
def first_index(input_string, substr):
    if substr in input_string:
        return input_string.find(substr)


# e) To count the occurrences of each word in a given string
def counter(input_string):
    dictionary = {}
    for i in input_string.split():
        dictionary[i] = dictionary.get(i, 0) + 1
    return dictionary


string = input("Enter String : ")
substring = input("Enter Substring : ")

print("Word with the longest length", longtest_word(string))
print("The frequencies of occurrence of particular character in the string", frequency_chr(string))
print("The string '{}' is {}".format(string, palindrome(string)))
print("The index of first appearance of the substring ", first_index(string, substring))
print("Count the occurrences of each word in a given string", counter(string))




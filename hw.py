#Shubhangi is having an array having n elements in unsorted order. This array is special as it can only have 0, 1 or 2 as the number. Help her sort this array (first O's then 1's then 2's) in O(n) time.
#Example:
#a = 10, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 11
#output: 000001111122


def sort012(numbers):
    zeros = 0
    ones = 0
    twos = 0

    # count
    for i in numbers:
        if i == 0:
            zeros = zeros + 1
        elif i == 1:
            ones = ones + 1
        else:
            twos = twos + 1

    # print in sorted order
    for i in range(zeros):
        print(0, end="")
    for i in range(ones):
        print(1, end="")
    for i in range(twos):
        print(2, end="")

# Example
a = [1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sort012(a)

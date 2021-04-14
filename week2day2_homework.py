# Exercise 1 - Given a list as a parameter,write a function that returns a list of numbers that are less than ten
# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

# Use the following list - [1,11,14,5,8,9]
# transform this list into a new list that is only numbers less than 10

numbers = [1,11,14,5,8,9]

the_numbers = [number for number in numbers if number < 10]

print(the_numbers)


# Exercise 2 - Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method

# using 2 lists - merge lists together or concat and sort
# expected: [1,2,3,4,5,6,7]

l_1 = [1,3,2]
l_2 = [4,6,5,7]

l_1.sort()
l_2.sort()

def merge_lists():
    print(l_1 + l_2)

print(merge_lists())
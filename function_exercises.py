# 1. Write a Python function to find the Max of three numbers
# def max_num(a, b, c):
# Solution1:
#     # return max([a, b, c])
#
# Solution2:
#     # lst = [a, b, c]
#     # m = lst[0]
#     # for i in range(1, len(lst)):
#     #     if lst[i] > m:
#     #         m = lst[i]
#     # return m
#
# n = max_num(11, 2, 41)
# print(n)

# 2. Write a Python function to sum all the numbers in a list

# def sum_list(lst):
#     result = 0
#     for num in lst:
#         result += num
#     return result
#
# s = sum_list([1, 10, 31, 22, 4, 5, 12.4])
# print(s)

# # 3. Write a Python function to multiply all the numbers in a list
# def multiply_args(*args):
#     result = 1
#     for num in args:
#         result *= num
#     return result
#
# r = multiply_args(5, 12, 4, 6)
# print(r)

# # 4. Write a Python program to reverse a string
# def str_reverse(phrase):
#     """
#     This function takes as argument a string and reverses it
#     :param phrase:
#     :return:
#     """
#     result = ""
#     for i in range (1, len(phrase) + 1):
#         result += phrase[-i]
#     return result
#
# words = ["hello", "world", "from", "python"]
# print(str_reverse.__doc__)
# for word in words:
#     text = str_reverse(word)
#     print(text)
#

# 5. Write a Python function tu calculate the factorial of a number ( a non negative integer)
# The function accepts the number as an argument.
def factorial(n):
    if n < 0:
        raise Exception("Negative number")
    if n == 0:
        return 0
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# r = factorial(3)
# print(r)

# 6. Verify if a number is in a given range
# def is_in_range(n, r):
#     return n in r
#
# res = is_in_range(4, range(12, 40))
# print(res)

# 7. Write a Python functionn that accepts a string and calculate the number of the
# upper case letters and lower case letters
# def upper_lower(s):
#     count_upper = 0
#     counter_lower = 0
#     for c in s:
#         if not c.isalpha():
#             continue
#         if c.islower():
#             counter_lower += 1
#         else:
#             count_upper += 1
#     return count_upper, counter_lower
#
# count = upper_lower("ABCdefG!!!!!*!(&^!@#&*!@#")
# print(count)

# 8. Write a Python function that takes a list and returns a lst with unique elementes of the first list
# Solution1
# def dedupe(lst):
#     return list(set(lst))
#
# unique = dedupe([1, 2, 3, 3, 4, 1, 2, 1, 24, 5, 6, 5, 5])
# print(unique)
#Solution2
def dedupe(lst):
    result = []
    for val in lst:
        if val not in result:
            result.append(val)
    return result

# 9. Write a Python function that takes a number as a parameter and check the number is prime or not
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    else:
        for x in range (2, n):
            if n % x == 0:
                return False
            return True

res = is_prime(9)
print(res)

# 10. Write a Python program to print the even numbers from a given list
def print_even(nums):
    for n in nums:
        if n % 2 == 0:
            print(n)

print_even(range(1, 20))
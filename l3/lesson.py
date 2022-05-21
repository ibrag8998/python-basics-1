from calendar import c


def print_smth():
    print("something printed")


# print_smth()



















def return_smth():
    return "something returned"


# return_smth()
# print(return_smth())


def pow(x, y):
    return x**y


def extended(l, *items):
    l = l[:]
    l.extend(items)
    # for item in items:
    #     l.append(item)
    return l


# some_l = [1, 2]
# print(extended(some_l, 3, 4))
# print(some_l)


def represent_object(object_name, **attributes):
    """
    Example:

    >>> represent_object("User", username="ibragdzh", age=20)
    <User: username=ibragdzh age=20>
    """
    
    representation = "<" + object_name + ":"
    for attr_name, attr_value in attributes.items():
        representation += " " + attr_name + "=" + str(attr_value)
    representation += ">"
    return representation


# print(represent_object("User", username="ibragdzh", age=20))


counter = 0


def counting_function():
    global counter
    counter += 1
    return counter


# print(counting_function())
# print(counting_function())
# print(counting_function())
# print(counting_function())


def fibonacci():
    # TODO: return 0 1 1 2 3 instead of 1 2 3 5 8
    a, b = 0, 1
    i = 0

    def next_number():
        nonlocal a, b, i
        
        if i <= 1:
            i += 1
            return i - 1
        
        a, b = b, a + b
        return b

    return next_number


f = fibonacci()
# print(f())
# print(f())
# print(f())
# print(f())
# print(f())


def function_as_argument(f, x, y):
    return f(x, y)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


# print(function_as_argument(add, 4, 5))
# print(function_as_argument(multiply, 4, 5))


# return_function
def upgraded_counting_function(start_from):
    counter = start_from

    def count():
        nonlocal counter
        counter += 1
        return counter

    return count


from_3 = upgraded_counting_function(3)
from_6 = upgraded_counting_function(6)
# print(from_3())
# print(from_3())
# print(from_6())
# print(from_6())
# print(from_6())
# print(from_3())

input = "global input"


def legb_demo():
    input = "enclosing input"

    def inner_function():
        input = "local input"

        # L      E          G       B
        # Local? Enclosing? Global? Built-in?
        return input

    return inner_function()


# print(legb_demo())

lambda a, b: a + b

# print(function_as_argument(lambda a, b: a + b, 4, 5))

###

some_map = map(lambda x: x**2, [1, 2, 3, 4, 5])
# print(some_map)
# print(list(some_map))

some_filter = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
# print(list(some_filter))

# x = 1
# (x % 2 == 0)? -> False
# x = 2
# (x % 2 == 0)? -> True

def missing_no(nums):
    i = 0
    delta = 1
    if nums[0] == 100:
        # i = 100
        # delta = -1
        nums = reversed(nums)
    for num in nums:
        if num != i:
            return i
        i += delta

# nums = list(range(0,101))
# nums.remove(5)
# print(missing_no(nums))

nums = list(reversed(range(0,101)))
nums.remove(100)
print(missing_no(nums))

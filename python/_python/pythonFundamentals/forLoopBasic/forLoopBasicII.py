# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]


def big(_list):
    for i in range(len(_list)):
        if _list[i] > 0:
            _list[i] = "big"
    return _list


print(big([-1, 3, 5, -5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it


def pos(_list):
    count = 0
    for i in range(len(_list)):
        if _list[i] > 0:
            count += 1
    _list[len(_list)-1] = count
    return _list


print(pos([1, 6, -4, -2, -7, -2]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7


def sum(_list):
    sum = 0
    for i in range(len(_list)):
        sum += _list[i]
    return sum


print(sum([6, 3, -2]))

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5


def average(_list):
    _average = 0
    for i in range(len(_list)):
        _average += _list[i]
    _average /= len(_list)
    return _average


print(average([1, 2, 3, 4]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0


def length(_list):
    return len(_list)


print(length([]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False


def min(_list):
    _min = _list[0]
    for i in range(len(_list)):
        if _list[i] < _min:
            _min = _list[i]
    return _min


print(min([]))

# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False


def max(_list):
    _max = _list[0]
    for i in range(len(_list)):
        if _list[i] > _max:
            _max = _list[i]
    return _max


print(max([]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }


def ult(_list):
    dict = {
        "sumTotal": 0,
        "average": 0,
        "minimum": _list[0],
        "maximum": _list[0],
        "length": len(_list)
    }
    for i in range(len(_list)):
        if _list[i] > dict["maximum"]:
            dict["maximum"] = _list[i]
        if _list[i] < dict["minimum"]:
            dict["minimum"] = _list[i]
        dict["sumTotal"] += _list[i]
    dict["average"] = dict["sumTotal"]/len(_list)
    return dict


print(ult([37, 2, 1, -9]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]


def reverse(_list):
    for i in range(round(len(_list)/2)):
        temp = _list[i]
        _list[i] = _list[len(_list)-1-i]
        _list[len(_list)-1-i] = temp
    return _list


print(reverse([37, 2, 1, -9]))

import math


# Implementation of Statistics with help of python function

def list_creation():
    lst = []

    x = input("Enter element of list: ")

    while x != "END":
        lst.append(int(x))
        x = input("Enter element of list: ")

    return lst


def short_list(old_list):
    input_list = []
    for k in old_list:
        input_list.append(k)
    len_list = len(input_list)
    sorted_list = []
    while len_list >= 1:
        lst_min = input_list[0]
        for i in range(1, len_list):
            if input_list[i] <= lst_min:
                lst_min = input_list[i]
        sorted_list.append(lst_min)
        input_list.remove(lst_min)
        len_list = len(input_list)

    return sorted_list


def mean_list(list):
    sum = 0
    for i in list:
        sum += i
    mean = sum / len(list)
    return mean


def median_list(old_list):
    s = sorted(old_list)
    len_list = len(s)
    if len_list % 2 == 0:
        index = int(len_list / 2)
        median = (s[index - 1] + s[index]) / 2
    else:
        index = math.ceil(len_list / 2)
        median = s[index - 1]
    return median


def mod_list(old_list):
    max_value = 0
    max_counter = 0
    for i in old_list:
        counter = 0
        for k in old_list:
            if i == k:
                counter += 1
        if counter > max_counter:
            max_counter = counter
            max_value = i
    return max_value, max_counter


def range_list(old_list):
    sort_lst = sorted(old_list)
    min_lst = sort_lst[0]
    max_lst = sort_lst[len(sort_lst) - 1]
    return min_lst, max_lst


def std_dev(old_list):
    mean = mean_list(old_list)
    sum_mean_diff = 0
    for i in range(len(old_list)):
        sum_mean_diff += (old_list[i] - mean) ** 2
    std_dev_final = sum_mean_diff / (len(old_list) - 1)
    var_lst = std_dev_final ** 0.5
    return std_dev_final, var_lst


old_list = list_creation()
print("Input List: ", old_list)
print("Sorted List : ", short_list(old_list))
print("Mean of List :", mean_list(old_list))
print("Median of List: ", median_list(old_list))
print("Mode of List: ", mod_list(old_list))
print("Min & Max :", range_list(old_list))
print("Standard Deviation & Variance :", std_dev(old_list))

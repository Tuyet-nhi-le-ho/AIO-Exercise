def max_kernel(num_list, k):

    sub_list = []
    result_of_max = []
    for element in num_list:
        sub_list.append(element)
        if len(sub_list) == k:
            result_of_max.append(max(sub_list))
            sub_list.pop(0)
    return result_of_max

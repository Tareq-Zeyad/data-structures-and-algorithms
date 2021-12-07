def insertion_sort(ls):
    if type(ls) is not list:
        return None

    reversed_list = ls
    for index, item in enumerate(reversed_list):
        j = index - 1
        temp = item

        while j >= 0 and temp < ls[j]:
            ls[j+1] = ls[j]
            j -= 1

        ls[j+1] = temp

    return reversed_list

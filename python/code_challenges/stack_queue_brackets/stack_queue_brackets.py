def validate_brackets(string):
    open_brackets = ["{", "[", "("]
    close_brackets = ["}", "]", ")"]
    result_list = []

    for i in string:
        if i in open_brackets:
            result_list.append(i)
        elif i in close_brackets:
            bracket_index = close_brackets.index(i)
            if result_list and (open_brackets[bracket_index] == result_list[len(result_list)-1]):
                result_list.pop()
            else:
                False
    if not result_list:
        return True
    else:
        return False

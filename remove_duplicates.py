
list1 = [1, 1, 1, 2, 1, 2, 1, 1, 1, 'hello', 'a', 'a', 'hello', 'apple', 'apple', 'hello']


def no_duplicates(array):
    output = []
    for item in array:
        if item not in output:
            output.append(item)
    return output


no_duplicates(list1)


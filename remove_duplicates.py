

array = [1, 1, 1, 2, 1, 2, 1, 1, 1, 'hello', 'a', 'a', 'hello', 'apple', 'apple', 'hello']
output = []
for item in array:
    if item not in output:
        output.append(item)
    print(output)




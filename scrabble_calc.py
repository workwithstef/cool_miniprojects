

one_point = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r']
two_point = ['d', 'g']
three_point = ['b', 'p', 'm', 'p']
four_point = ['f', 'h', 'v', 'w', 'y']
five_point = ['k']
eight_point = ['j', 'x']
ten_point = ['q', 'z']


def word_calc(word):
    score = 0
    for letter in word:
        if letter in one_point:
            score += 1
        elif letter in two_point:
            score += 2
        elif letter in three_point:
            score += 3
        elif letter in four_point:
            score += 4
        elif letter in five_point:
            score += 5
        elif letter in eight_point:
            score += 8
        elif letter in ten_point:
            score += 10
    return score


# TEST CODE
word_calc('xylophone')
expected_result = 24

print(word_calc('xylophone') == expected_result)

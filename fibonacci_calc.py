
fibonacci = [0, 1]
user_n_terms = input('How many values do you want? ')
while True:
    fibonacci.append(fibonacci[-2] + fibonacci[-1])
    print(fibonacci)

    if len(fibonacci) == int(user_n_terms):
        break

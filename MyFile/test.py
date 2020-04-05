sq_list = [x**2 for x in range(10)]  # this produces a list of squares

print(sq_list)

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares
print(sq_iterator)
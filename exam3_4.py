a = [1, 1, 2, 3, 4, 9]
b = [1, 2, 3, 5, 6, 1, 4, 9]

def get_intersection(a, b):

    result = [i for i in a if i in b]
    return result

print(get_intersection(a, b))


lista1 = [3, 7, 8, 12, 4, 33, 90, 45]
lista2 = [15, 7, 4, 10, 2, 33, 93, 65]


def func(one: list, two: list) -> list:
    new_list = one + two
    new_list = set(new_list)
    RetList = []
    for x in new_list:
        RetList.append(x**3)

    return RetList


print(func(lista1, lista2))

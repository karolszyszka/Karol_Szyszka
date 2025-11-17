lista = [4,7,12,3,9,6,10,2]
def func(one:list, two:int)->bool:
    for x in one:
        if x == two:
            return True
print(func(lista, 6))
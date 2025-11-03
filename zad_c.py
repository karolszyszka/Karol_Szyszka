list =range(17,27)
def funcC(numbers): #Funkcja wyswietla parzyste liczby
    for x in numbers:
        if x % 2 == 0:
            print(x)
    return "Koniec"
print(funcC(list))
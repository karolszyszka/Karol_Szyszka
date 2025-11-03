def funcB(num1,num2,num3,num4,num5): #Funkcja wczytuje 5 liczb i mnoży je przez 2
    nums = list([num1,num2,num3,num4, num5])
    MlisNums =[x*2 for x in nums] #metoda z wykorzystaniem list składanych
    # return MlisNums
    MforNums = []
    for x in nums: #Metoda z wykorzystaniem petli for
        MforNums.append(x*2)
    return MforNums
print(funcB(1,2,3,4,5))
def fun(str1, str2):
    cont = 0
    for i in range(100):
        if i % 3 == 0:
            print(str1)
            cont += 1
        elif i % 5 == 0:
            print(str2)
            cont += 1
        elif i % 5 == 0 & i % 3 == 0:
            print(str1 + " " + str2)
            cont += 1
        else:
            print(i)

    return cont
print("Total veces: ", fun("HOLA", "PATATA"))
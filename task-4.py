
#Printing Common elements in both Lists
def printCommon(a,b):
    final = []
    for i in a:
        if i in a and i in b:
            final.append(i)

    print(final)



def main():
    lis1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lis2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    printCommon(lis1,lis2)


main()
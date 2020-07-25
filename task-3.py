

#Find Divisors
def printDivisors(num):
    List = []
    for i in range(1,num+1):
        if num%i == 0:
            List.append(i)
    
    #Print Whole List
    print(f"{List}")

def main():
    try:
        num = int(input("Enter Number: "))
    except:
        print("Invalid Input!")
        return
    printDivisors(num)

main()
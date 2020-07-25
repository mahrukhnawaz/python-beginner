
#Function to find out if list element is less then 5 or not
def check(num):
    return num < 5

def main():
    List = []
    for i in range(10):
        try:
            num = int(input("Enter Numbers: "))
            List.append(num)
        except:
            print("Invalid Input!")
            return
    for i in List:
        if check(i):
            print(f"{i}")


main()

#Find Out even or odd
def find(num):
    if num % 2 > 0:
        print(f"Give number {num} is even!")
    else:
        print(f"Give number {num} is odd!")

#main fucnction with execption handelling
def main():
    try:
        num = int(input("Enter Number: "))
    except:
        print("Invalid Input!")
        return
    #if input is Fine
    find(num)


#Main Call Inefficuent way
main()
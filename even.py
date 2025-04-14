#printing even numbers from 1 to 20

while True:
    start = int(input("Enter the beginning number: "))
    end = int(input("Enter the ending number: "))

    if start > end:
        print("Beginning number cannot be greater than ending number!")
    else:
        print("Even numbers in the range:")
        for i in range(start, end + 1):
            if i % 2 == 0:
                print(i)

    choice = input("Do you want to run the program again? (yes/no): ").lower()
    if choice != "yes":
        print("👋 Goodbye!")
        break

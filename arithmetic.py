# Arithmetic operations between two numbers
while True:
    input_no1 = int(input("Enter the first number: "))
    input_no2 = int(input("Enter the second number: "))
    input_opr = input("Choose operation to perform (+, -, *, /): ")

    if input_opr == "+":
        answer = input_no1 + input_no2
        print("Answer:", answer)
    elif input_opr == "-":
        answer = input_no1 - input_no2
        print("Answer:", answer)
    elif input_opr == "*":
        answer = input_no1 * input_no2
        print("Answer:", answer)
    elif input_opr == "/":
        if input_no2 != 0:
            answer = input_no1 / input_no2
            print("Answer:", answer)
        else:
            print("Division cannot be done with denominator 0")
    else:
        print("Invalid operation chosen.")

    choice = input("Do you want to continue the program for another operation (y/n)? ").lower()
    if choice != "y":
        print("Bye!")
        break

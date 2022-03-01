while 1 > 0:
    def calculater(number_one, number_two, operation):
        if operation == 1:
            print(number_one + number_two)
        elif operation == 2:
            print(number_one - number_two)
        elif operation == 3:
            print(number_one * number_two)
        elif operation == 4:
            if number_two == 0:
                print("Error")
            else:
                print(number_one / number_two)
        elif operation == 5:
            print(number_one % number_two)
        else:
            print("Select an answer")
    number_one = int(input("Enter the first number: "))
    number_two = int(input("Enter the second number: "))
    operation = int(input("1. +\n2. -\n3. *\n4. /\n5. %\n"))
    
    calculater(number_one, number_two, operation)
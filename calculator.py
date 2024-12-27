try:
    while(True):
        print("""Please Select Operation
        1. Addition
        2. Substraction
        3. Multiplication
        4. Division""")
        class Calculator():
            def Add(self,a,b):
                print("The Addition of {},{} = {}".format(a,b,a+b))

            def Sub(self,a,b):
                print('The Subtraction of {},{} = {}'.format(a,b,a-b))

            def Mul(self,a,b):
                print('The Multplication of {},{} = {}'.format(a,b,a*b))

            def Div(self,a,b):
                print('The Division of {},{} = {}'.format(a,b,a/b))
        cal=Calculator()
        a=int(input("Enter 1st value: "))
        b=int(input("Enter 2nd value: "))
        inp=int(input("Please select option to perform Operations: "))
        if inp == 1:
            cal.Add(a,b)
        elif inp==2:
            cal.Sub(a,b)
        elif inp==3:
            cal.Mul(a,b)
        elif inp == 4:
            cal.Div(a,b)
            print("-"*50)
        else:
            print("Please Select Correct Option")
        retry = input("Do you want to perform another operation? (y/n): ").lower()
        if retry == "n":
            print("Thank you")
            break
except TypeError:
    print("Dont use alphabets use number")
except ZeroDivisionError:
    print("0 Cannot by Divisible")

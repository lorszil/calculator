print ("Welcome to my calculator!")

no1 = input("Enter the first number:")
if no1.isdigit():
    func=input("Enter an operation (-+*/):")
    no2=int(input("Enter the second number:"))
    no1=int(no1)

    if func=="+":
        ans=no1+no2
        print ("Result: {}" .format (ans))
    else:
        False

    if func=="-":
        ans=no1-no2
        print ("Result: {}" .format (ans))
    else:
        False

    if func=="*":
        ans=no1*no2
        print ("Result: {}" .format (ans))
    else:
        False

        if func=="/":
            ans=no1/no2
            print ("Result: {}" .format (ans))
        else:
            False
else:
    print ("Try again!")

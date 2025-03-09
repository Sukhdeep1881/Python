x = int(input("Enter data Exercise number: "))

match x:
    case 1:
        print(x," is data Exercise match")

    case 2:
        print(x," is data Exercise match")

    case 3:
        print(x," is data Exercise match")

    case 4 if x%2==0:
        print(x,"is x%2==0 and is data Exercise match")

    case _ if x<10:
        print(x,"is x<10 and is data Exercise match")
    case _ if x!=90:
        print("x is not 90")
    case _ if x==90:
        print(x," is 90")
    case _:
        print(x)
class calc:

    def pow(self,a,b):
        return a**b

cal=calc()

while True:

    print("6.Power")


    choice=input("Enter your choice(1-6): ")

    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))


    if choice=="6":
        print("Result: ",cal.pow(a,b))

    else:
        print("Error!!!!")
class calculator:
      def add(self,a,b):
           return a + b
      def sub(self,a,b):
           return a - b
      def mul(self,a,b):
           return a * b
      def div(self,a,b):
           return a % b
           

calc=calculator()

while True:
    print("1.addition")
    print("2.subtraction")
    print("3.multiply")
    print("4.division")
    print("5.exit")
    
    choice=input("enter choice:")
    
    if choice == "5":
      print("Existing calculator. Thank you")
      break
      
    a = int(input("enter the number 1:"))
    b = int(input("enter the number 2:"))
    
    if choice == "1":
      print("Result:",calc.add(a,b))
    elif choice == "2":
      print("Result:",calc.sub(a,b))
    elif choice == "3":
      print("Result:",calc.mul(a,b))
    elif choice == "4":
      print("Result:",calc.div(a,b)) 
      
    else:
        print("error")
    

    
    



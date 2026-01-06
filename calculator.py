class calculator:
      def add(self,a,b):
           return a + b
      def sub(self,a,b):
           return a - b

calc=calculator()

while True:
    print("1.addition")
    print("2.subtraction")
    print("3.exit")
    
    choice=input("enter choice:")
    
    if choice == "3":
      print("Existing calculator. Thank you")
      break
      
    a = int(input("enter the number 1:"))
    b = int(input("enter the number 2:"))
    
    if choice == "1":
      print("Result:",calc.add(a,b))
    elif choice == "2":
      print("Result:",calc.sub(a,b)) 
      
    else:
        print("error")
    

    
    



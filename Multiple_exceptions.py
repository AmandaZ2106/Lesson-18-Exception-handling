try:
    num1,num2=eval(input("Please enter two numbers seperated by a comma:"))
    div=num1/num2
    print("The result is:",div)
except ZeroDivisionError:
    print("The 1st number cannnot be divided by 0!")
except SyntaxError:
    print("The comma is missing, please place a comma between the numbers")
except:
    print("Wrong input")
else:
    print("No exceptions!")
finally:
    print("The code will run no matter what!!")                

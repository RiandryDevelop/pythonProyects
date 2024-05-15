#This is a BASIC calculator
import functions
my_calculator = functions.Math_functions()

def calculating():
      # Asking for the values require
      operation = str(input("Introduce the operation:(+),(-),(*),(/)\n:"))
      number1 = int(input("First Number: "))
      number2 = int(input("Second Number: "))

      # Choosing one of the options available
      match operation:
            case '+':
                  print("The result of the addiction is: ", my_calculator.addiction(number1, number2))
            case '-':
                  print("The result of the subtraction is: ", my_calculator.subtraction(number1, number2))
            case '*':
                  print("The result of the multiplication is: ", my_calculator.multiply(number1, number2))
            case '**':
                  print("The result of the potentiating is: ", my_calculator.potenciation(number1, number2))
            case '/':
                  print("The result of the division is: ", my_calculator.divide(number1, number2))
            case _:
                  print("Error, This operation does not exist")


# Asking to the user if him/her/hers/theirs ect want to keep using the app
def ContinuatingCalculating():
      continueProcess = str(input("Do you want to continue ?:"))

      if continueProcess.upper() == "YES":
            continuating = True

      else:
            continuating = False

      while continuating == True:
            Calculating()
            ContinuatingCalculating()

            if continuating == False:
                 break

      else:
            breakpoint(print("Thank for using our APP"))

Calculating()
ContinuatingCalculating()




# n = int(input("Number:"))
# def factor(numero):
#       if numero == 1:
#             return 1
#       else:
#             return (numero * (factor(numero-1)))
#
#
# print(factor(n))
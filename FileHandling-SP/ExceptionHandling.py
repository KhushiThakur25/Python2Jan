# Exception Handling
# 1.try-logic
# 2.except-error
# 3.else - option
# 4.finally - always execute....

try:
    num_1 = int(input("Enter the number 1.."))
    num_2 = int(input("Enter the number 2.."))

    add = num_1 + num_2
    
    div = num_1/num_2
    sub = num_1 - num_2
    

except ValueError :
    print("Please enter valid input..")
except ZeroDivisionError as msg:
    print(msg)
except Exception as msg:
    print(msg)
else:
    print("Sum is",add)
    print("Sub is",sub)
    print("Div is",div)
finally:
    print("I'm always executed..")



input1 = int(input("Enter the first number: "))
input2 = int(input("Enter the second number: "))

try : 
    input1/input2
    return ("The result is: ", input1/input2)

except ZeroDivisionError as zde:
    return ("Error: ", zde)
except TypeError as te:
    return ("Error: ", te)
except Exception as e:
    return ("An unexpected error occurred: ", e)
finally:
    print("This will always execute.")
    

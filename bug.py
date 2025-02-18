def function_with_uncommon_error(a, b):
    if a == 0:
        return 0  #This is an uncommon error: it doesn't handle other exceptions
    return b / a

result = function_with_uncommon_error(0, 10)
print(result) #This will print 0
result = function_with_uncommon_error(10,0)
print(result) #This will raise ZeroDivisionError
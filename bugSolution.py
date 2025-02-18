def function_with_robust_error_handling(a, b):
    try:
        if a == 0:
            return 0
        return b / a
    except ZeroDivisionError:
        return float('inf')  #Or handle it appropriately
    except TypeError:
        return None #Or handle it appropriately
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

result = function_with_robust_error_handling(0, 10)
print(result) #This will print 0
result = function_with_robust_error_handling(10, 0)
print(result) #This will print inf
result = function_with_robust_error_handling("a",10)
print(result) #This will print None
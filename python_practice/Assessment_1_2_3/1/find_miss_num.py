
def missing_number(arr): 
    n = len(arr) 
    total = (n + 1)*(n + 2)/2
    sum_of_arr = sum(arr) 
    return total - sum_of_arr 
  
arr = [1, 2, 3, 5] 
missing = missing_number(arr) 
print(missing)
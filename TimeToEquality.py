def min_time_to_make_equal(A):
    total_elements = len(A)
    total_sum = sum(A)
    max_val = max(A)
    
    min_time = (total_elements * max_val) - total_sum
    
    return min_time

A=list(map(int,input().split()))
output = min_time_to_make_equal(A)
print(output) 


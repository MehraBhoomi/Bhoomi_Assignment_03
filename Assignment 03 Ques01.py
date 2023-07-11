# Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)

# Expected Output : 20

# Explanation:
# Summation should like 8+2+3+0+7 = 20

# Solution

sample_list = [8,2,3,0,7]
sample_tuple = (9,1,6,3,8)

def Sum(a):
    count=0
    for i in a:
        count = count+i
    print(count)
    return ''

Sum(sample_list)
Sum(sample_tuple)

# Output: 
# 20
# 27
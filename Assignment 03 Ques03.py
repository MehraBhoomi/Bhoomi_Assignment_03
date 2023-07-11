# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

# Sample String : 'The quick Brow Fox'

# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

# Solution:

s = input("Enter a string: \n")
sample_string = "The quick Brow Fox"
def upplow(a):
    lower_count = 0
    upper_count = 0
    print(a)
    for i in a:
        if i.islower():
            lower_count = lower_count+1
        elif i.isupper():
            upper_count = upper_count+1

    print ("No. of Lower case characters in given string :",  lower_count)
    print ("No. of Upper case characters in given string :",  upper_count)
    return ""

upplow(s)
upplow(sample_string)



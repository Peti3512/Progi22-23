
# Python3 code to demonstrate working of
# Uppercase Nth character
# Using upper() + string slicing
 
# initializing string
test_str = "GeeksforGeeks"
 
# printing original string
print("The original string is : " + str(test_str))
 
# initializing N
N = 4
 
# Using upper() + string slicing
# Uppercase Nth character
res = test_str[:N] + test_str[N].upper() + test_str[N + 1:]
 
# printing result
print("The string after uppercasing Nth character : " + str(res))
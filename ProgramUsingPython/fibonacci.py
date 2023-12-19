#Write a Program for the first 10 numbers of Fibonacci series.
# Example




'''
To print the fibonacci series which the result will be added to previous number 
'''
# 0 1 1 2 3 5 8 13
a=0
b=1
# sum=a+b
# b=sum
# sum
print("Output:",end="")

# range is writtain 8 because initialy we have taken a=0 and b=1 and total is 10
for i in range(8):
    sum=b+a
    a=b
    b=sum
    print(f"{sum}, ",end="")

# print(sum)
    
# same can be done usign recursion 
    
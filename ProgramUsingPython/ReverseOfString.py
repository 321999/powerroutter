'''
Write a program to reverse a string.
Example:
○ Input : Welcome
○ Output : emoclew
'''

# we are going to use the concept of slicing
Input= "Welcome"
'''
concept of slicing used here
[start:stop:incr/decr]
'''
print(f"Input: {Input}\nOutput: ",Input[-1:-len(Input)-1:-1])
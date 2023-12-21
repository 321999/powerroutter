'''
Write a program to reverse a string.
Example:
○ Input : Welcome
○ Output : emoclew
'''

# we are going to use the concept of slicing
Input= "Welcome"
print(f"Input: {Input}\nOutput: ",Input[-1:-len(Input):-1])


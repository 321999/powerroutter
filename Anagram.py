'''
Write a program to check if two strings are Anagrams?
Example:
○ Input : Welcome
○ Output : ceelmow
'''
str1="Welcome"
str2="ceklmow"
b=False
if len(str1)==len(str2):
    for i,j in zip(str1,str2):
        if i in str2 and j in str1:
            print(f"{i}={str2.index(i)},{j} {str1.index(j)}")
            b=True
    if b:
        print("The givne input is anagram")
else:
    print("The given string are not anagram")
# for i,j in zip(str1,str2):
#     print(i,j)
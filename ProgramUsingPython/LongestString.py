# Write a Java program to find the longest substring from a given string that doesn’t
# contain any duplicate characters
# Input=" Welcome to PowerRouter"
# max=Input[0]
# # {  ÷ for i in Input.split()}
# st="welcom"
# uniqueString=[]
# print(Input.split())
# for j in Input.split():
#     newList=[]
#     for i in j:
#         if i not in newList:
#             newList.append(i)
#         # print(uniqueString)
#         else:
#             print("not unique")
#             newList=[]
#     print(newList)
#     uniqueString.append("".join(newList))    
# print(uniqueString)
# print(uniqueString)

# for i in Input.split():
#     l=[]
Input = "Welcome kis to PowerRouter"
# max = Input[0]
# first we are going to make the list of only non duplicates entry
uniqueString = []
'''
Input.split()  
this is done to convert the string to list format 
'''
for j in Input.split():
    # this newlist is  going to initialise for each word of string and it only stores the string which do have duplicates
    newList = []
    for i in j:
        # logic to store only the non duplicate entry
        if i not in newList:
            newList.append(i)
        else:
            # print("not unique")
            newList = []
            break
    uniqueString.append("".join(newList))

    # print(newList)
#from the unique word from list,know i will find the maximum length string 
# logic to find the maximul length string from an array 
max=len(uniqueString[0])
for i in uniqueString:
    if len(i)>max:
        max=len(i)
# to find the maximum length string 
for i in uniqueString:
    if len(i)==max:
        print(f"OUTPUT: {i}")




# print(uniqueString)




#     for j in i:
#         if j not in l:
#             l.append(j)
#         else:
#             break
#         continue

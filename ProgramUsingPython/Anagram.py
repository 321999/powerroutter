
# print(str3+"+",str4)
# b=False
# for i,j in zip(str1,str2):
#     print(i,j)

# if 'w' in str2:
#     print(f"it is presetn {str2.index('w')}")
str1=st1="welcome"
str2=st2="ceelmow"
b=True
if len(str1)==len(str2):
  for i,j in zip(str1,str2):
    # print(i,j)
    if i in st2 and j in st1:
    #   print(i,j)
      b=True
    else:
      b=False
      break

if b:
    print("Anagram")
else:
    print("Not Anagram")
        
        











  # for i in str1:
  #     if i in st2:
  #       print(i,st2.index(i))
  #       b=True
  #     else:
  #           b=False
  #           print("1ka ",i)
  #           break
  # for j in str2:
  #     if j in str1:
  #         b=True
  #     else:
  #           print(j)
  #           b=False
  #           break



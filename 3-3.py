 #checking vowels in the string:

# string1="Welcome 25r to 27r".lower()
# res_str=" "
# for  i in string1:
#     if i in "aeiou":
#         pass
#     else:
#         res_str=i+res_str

# print(res_str) 

#finding largest Word in the string:

# string2="Google doc is better than word doc"
# new_str=string2.split()

# large_string=new_str[0]
# res_list=[]

# for i in new_str:
#     if len(i)>=len(large_string):
#        if len(i)>len(large_string):
#             res_list.clear()
#     large_string=i
#     res_list.append(i)
# print(res_list)




# finding largest palindrome in string:

# input="abccbc"

# def check_palindrome(input):
#     return input==input[::-1]

# max_string=input[0]
# for i in range(len(input)):
#     for j in range(i,len(input)+1):
#         sub_str=input[i:j]
#         if check_palindrome(sub_str):
#             if len(sub_str)>len(max_string):
#                 max_string=sub_str
#                 print(max_string)



str1="takeuforward"
str2="forward"

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i]==str2[j]:
            pass
            spy =True
        else:
            spy=False
            break
        if spy==True:
            print("substring Found")
 
   



# Recursion-a function callling itself with different arguments

#Factorial:

# def factorial(n):
#          if n==1 or n==0:
#              return 1
#          return  n* factorial(n-1)

# print(factorial(5))

# #Sumof Digits: (loop)

# # num1=123456
# # sum =0
# # while num1>0:
# #      rem=num1%10
# #      sum+=rem
# #      num1=num1//10
# # print(sum)



# def sum_of_digits(num2):
#        if num2==0:
#               return 0
#        rem=num2%10
#        return rem+sum_of_digits(num2//10)
       
# print(sum_of_digits(123))







#reverse string


# name="siva"
# name1=""
# for i in name:
#     #    print(i)
#        name1=i+name1
# print(name1)

#by Recursion

# name2="reddy"

#  def reverse(name2):
#     if len(name2)<=0 :
#           return ''
#     return name(-1)+name(:-1)


str="level"
# if str[0]==str[len(str)-1]:
#     print("palindrome")
# else:
#     print("dbmxvmnv")
# print(len(str)-1)



def palindrome(str1):
    if len(str)<=0:
        return ''
    else:
        return str[0]==str[-1] and 
        palindrome(str[1:-1])
print(palindrome("madam"))






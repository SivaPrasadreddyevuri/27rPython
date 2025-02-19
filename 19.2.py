# Given array of N integer, the task is to replace each element of the array  by its rank in the array
#    Input: 20 15 26 2 98 6       Output:4 3   5   1  6 2
# Explanation: when the array is sorter 2 rank is 1, 6 rank is 2 , 15 rank is 3

# list=[20,15,26,2,98,6]
# list1=sorted(list)
# # list.sort()
# print(list1)
# print(list)
# list2=sorted(list,reverse=0)
# print(list2)



# res=[]
# for i in list:
#   new=list1.index(i)
#   res.append(new)

# print(res)
# 18) arrange first half in ascending order and second half in descending order
#      input: 8 7 1 6 5 9           output: 1 5 6 9 8 7

list1=[8,7,1,6,5,9] 
list1.sort()

low=(len(list1) -1)//2 +1
high=len(list1)-1
while low<high:
    list1[low],list1[high]=list1[high],list1[low]
    low+=1
    high-=1

print(list1)   

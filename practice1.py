list1=[]
n=int(input("enter the no of elements in list"))
for i in range(0,n):
    num=int(input())
    list1.append(num)
print(list1)    
for i in range(0,n):
    for j in range(0,n-i-1):
        if(list1[j]>list1[j+1]):
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp

for i in range(0,n):
    small=list1[1]
print(small)    
        
            
            

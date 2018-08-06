a=set()
b=set()
for i in range(1,11):
    num=i*i
    a.add(num)
print(a)
for i in range(1,11):
    num1=i*i*i
    b.add(num1)
print(b)
a.update(b)
print(a)
a.remove(64)
print(a)
a.add(10001)
print(a)
    

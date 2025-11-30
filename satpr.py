a='harshad@123 mahesh@123'
a_count=0
b_count=0
c_count=0

for i in a:
    if i.isalpha():
        a_count +=1
    if i.isdigit():
        b_count+=1
    if not i.isalnum() and not i.isspace():
        c_count+=1
        
        
print(a_count,
b_count,
c_count,)

#readline ,
fp=open("test.txt")
data=fp.readline()
print(data)
length=len(data)
print(length)
s=data.split()
print(s)
print(len(s))



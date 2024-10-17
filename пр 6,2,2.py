n=int(input())
x=[]
y=[]
z=[]
for i in range(n):
    print('введите',i,'элемент')
    x.append(int(input()))
for i in range(n):
    if x[i]>0:
        y.append(x[i])
    if x[i]<0:
        z.append(x[i])
print(x)
print(y)
print(z)
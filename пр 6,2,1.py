n=int(input())
a=[]
for i in range(n):
    print('введите',i,'элемент')
    a.append(int(input()))
mini=a[0]
for i in range(n):
    if mini>a[i]:
        mini=a[i]
        print(mini)
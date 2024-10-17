
def s(a,b):
    s=a*b
    return s
a=[]
for i in range(3):
    print('Ведите стороны',i,'-го треугольника:')
    a=int(input('a:'))
    b=int(input('b:'))
    a.append(s(a,b))
for i in range(3):
    print('площадь',i,'-го треугольника {:.2f}'.format(a[i]))
    

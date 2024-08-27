# DemoListTuple.py

lst = ['red','blue','grean']

print(len(lst))
print(lst)
lst.append('white')
lst.insert(1, 'pink')
print(lst)
print(lst.count('red'))
print(lst.index('blue'))
lst.sort()
print(lst)
lst.reverse()
print(lst)

print('---tuple---')

#함수정의
def times(a,b):
    return a+b, a*b

#호출
result = times(3,4)
print(result)

print('id:%s, name:%s' % ('kim', '김유신'))

args = (5,6)
print(times(*args))




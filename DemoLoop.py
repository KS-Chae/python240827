# DemoLoop.py

value = 5
while value > 0:
    print(value)
    value -= 1

print('--- for in 루프 ---')
lst = [10, 20, 30]
for i in lst:
    print('Item:{0}'.format(i))

def getBiggeThan20(i):
    return i > 20

lst = [10,25,30]
iterL = filter(getBiggeThan20, lst)
for item in iterL:
    print(item)

iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)

#DemoOS.py

from os.path import *

filename = 'python.exe'
print(abspath(filename))
print(basename('c:/work/demo.txt'))

if exists('c:/python310/python.exe'):
    print('파일크기:{0}'.format(getsize('c:/python310/python.exe')))
else:
    print('파일 없음')

import os
print('운영체제 이름:{0}'.format(os.name))
print('환경변수:{0}'.format(os.environ))
os.system('notepad.exe')


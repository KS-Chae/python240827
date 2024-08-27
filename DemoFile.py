# DemoFile.py


f = open('c:\\work\\test.txt', 'wt', encoding='utf-8')
f.write('첫번째라인\n두번째라인\n세번째라인\n')
f.close()

f = open(r'c:\work\test.txt', 'rt', encoding='utf-8')
result = f.read()
f.close()

print(result)

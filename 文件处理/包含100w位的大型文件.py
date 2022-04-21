fname = 'd:/programs/code/文件处理/file/pi.txt'
with open(fname) as fobject:
    lines = fobject.readlines()
pistring = ''
for line in lines:
    pistring += line.strip()
print(pistring[:50] + '...')
print(len(pistring))
def r(a='',b='',c=''):
    info_r = {}
    if a:
        info_r['A'] = 0
        info_r['B'] = a
        info_r['C'] = 0
    else:
        info_r['A'] = 0
        info_r['B'] = 0
        info_r['C'] = 0
    if b:
        info_r['A'] = a
        info_r['B'] = b
        info_r['C'] = 0
    if c:
        info_r['A'] = a
        info_r['B'] = b 
        info_r['C'] = c
    return info_r
info_text = r(1)
print(info_text)
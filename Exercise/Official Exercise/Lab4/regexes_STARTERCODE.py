
# COM3110/4155/6155: Text Processing
# Regular Expressions Lab Class

import sys, re

#------------------------------

testRE = re.compile('(logic|sicstus)', re.I)

#------------------------------

with open('RGX_DATA.html') as infs: 
    linenum = 0
    for line in infs:
        linenum += 1
        if line.strip() == '':
            continue
        print('  ', '-' * 100, '[%d]' % linenum, '\n   TEXT:', line, end='')
    
        m = testRE.search(line)
        if m:
            print('** TEST-RE:', m.group(1))

#        mm = testRE.finditer(line)
#        for m in mm:
#            print('** TEST-RE:', m.group(1))


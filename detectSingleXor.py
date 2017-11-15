chunk = []
fp = open('basic3.txt','r')
with open(fname) as f:
    while True:
    chunk[i] = fp.read(n)
    i++
    if chunk == '':
        break
        process(chunk)    
    
for i2 in range(len(chunk)):
    for i3 in range(len(chunk)):
        if (int(chunk[i2], 16) ^ int(chunk[i3], 16)) == (int(chunk[i3], 16)) ^ (int(chunk[i3], 16):
                return True


s='b'+''.join(format(ord(c),'07b')for c in input());r=''
for i,b in enumerate(s[1:]):r+='0'if b==s[i]else' '+'00 0'[int(b):]
print(r[1:])

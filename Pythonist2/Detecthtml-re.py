import sys
N = input()
full = sys.stdin.read().replace('\n',' ')
#comments
t = full.index('<!--')
if t != -1: full = full[:t] + full[full.index('-->')+3:]

att = []
i = j = 0
while i < len(full):
    #closing tags
    if full[i:i+1] == '</':
        i = full.index('>',i+1)
        continue
    if full[i] == '<':
        x = full.index('>',i+1)
        y = full.index(' ',i+1)
        if y == -1: t = x
        else: t = x if x<y else y
        if full[i+1] != '/': att.append([full[i+1:t],False])
        i = t
        continue
    if full[i] == '>':
        i = full.index('<',i+1)
        continue
    if full[i] == ' ':
        while full[i+1] == ' ': i +=1
        t = full.index('=',i+1)
        a = full[i+1:t]
        x = full.index('"',t+3)
        b = full[t+2:x]
        att.append([a,b])
        i = x+1
        continue
    i = len(full)
#printing
for l in att:
    print (l[0] if l[1] == False else '-> ' + l[0] + ' > ' + l[1])

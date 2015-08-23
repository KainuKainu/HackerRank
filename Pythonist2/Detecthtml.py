import sys
N = input()
full = list(sys.stdin.read().split())
#comments
tmp = full.index('<!--')
if tmp != -1:
    full = full[:tmp] + full[full.index('-->')+1:]
#tags & atts
att = []
for i in range (len(full)):
    if full[i].startswith('</'): continue
    if full[i].startswith('<'):
        full[i] = (full[i])[1:full[i].find('>')] \
                if full[i].find('>') != -1 else (full[i])[1:]
        att.append([full[i], False])
    else:
        tmp = full[i].find('=')
        att.append([(full[i])[:tmp], \
                (full[i])[tmp+2:full[i].find('"', tmp+2)]])
#printing
for l in att:
    print (l[0] if l[1] == False else '-> ' + l[0] + ' > ' + l[1])

N,M = map(int, input().split())
for i in range (1,N,2): print('-'*int((M-i*3)/2) + '.|.'*i + '-'*int((M-i*3)/2))
print ('-'*int((M-7)/2) + 'WELCOME' + '-'*int((M-7)/2))
for i in range (1,N,2): print('-'*int((M-(N-i-1)*3)/2) + '.|.'*(N-i-1) + '-'*int((M-(N-i-1)*3)/2))

'''
a: 5분
b: 1분
c: 10초
t: 요리시간

최소버튼만 누르게
맞출 수 없다면 -1
'''

import sys
cnt=[0,0,0]
t = int(sys.stdin.readline())
time = [300,60,10]
for i in range(3):
    cnt[i] += t//time[i]
    t%=time[i]
if t != 0:
    print(-1)
else:
    print(cnt[0], cnt[1], cnt[2])    


'''
#시간초과 ..ㅎㅎ
import sys
cnt0, cnt1 = 0,0

def fibonacci(n):
    global cnt0, cnt1
    if n == 0:
        cnt0+=1
        return 0
    elif n == 1:
        cnt1+=1
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    fibonacci(k)
    print(cnt0,cnt1)
    cnt0, cnt1 = 0,0
'''

'''
점화식
one[i]=one[i-1]+one[i-2]
zero[i-1]=zero[i-1]+zero[i-2]
'''
import sys
zero=[1,0,1]
one=[0,1,1]
for i in range(3,42):
        zero.append(zero[i-1]+zero[i-2])
        one.append(one[i-1]+one[i-2])
t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    print(zero[k],one[k])

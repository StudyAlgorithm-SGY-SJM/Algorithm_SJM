"""
9095 1,2,3 더하기
n (0< n <11)
t 입력 갯수
점화식
1번 1
2번 2
3번 4
(n>3) n번 (n-1번+1씩)+(n-2번+2씩)+(n-3번+3씩)
"""

t = int(input())
num= [0 for _ in range(11)]
num[1]=1 #시작값
num[2]=2
num[3]=4
for i in range(4,11):
    num[i] = num[i-1]+num[i-2]+num[i-3] #점화식

for k in range(t):
    n=int(input())
    print(num[n])
        

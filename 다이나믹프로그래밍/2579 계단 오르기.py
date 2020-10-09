'''
2579 계단오르기
n: 300이하의 자연수
각 계단의 점수: 10,000이하의 자연수

ex) stairs = [10,20,15,25,10,20]
dp(0) = 10
dp(1) = 10 + 20
dp(2) = max(10+15, 20+15) //세 칸을 다 밟을 수 없으므로
dp(3) = max(dp(1)+25, dp(0)+15+25)
.
.
.
점화식 : dp(i) = max(dp(i-2)+stairs[i], dp(i-3)+stairs[i-1]+stairs[i]) (i>2)
'''

import sys
n = int(sys.stdin.readline())
stairs = [0]*(n+3) # 3개의 0을 넣은 이유는 n이 3이하일때도 가능하게 하기위해~
for i in range(n):
    stairs[i]= int(sys.stdin.readline())  
dp = [stairs[0]]
dp.append(stairs[0]+stairs[1])
dp.append(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))
for i in range(3,n):
    dp.append(max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i]))
print(dp[n-1])    

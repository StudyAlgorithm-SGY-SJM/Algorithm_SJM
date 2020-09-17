"""
2839 설탕배달
Nkg 배달 (3<= N <= 5000)
봉지 종류: 3kg/5kg
minimum 봉지 수
예외처리: -1
"""

N = int(input())
cnt = 0
M = 0

#5kg 처리
cnt = N//5 
M = N % 5
#나머지 3kg으로 나눔
while M != 0:
    if M % 3 == 0:
        cnt += M//3
        break
    cnt -= 1 #3kg으로 안나누어 질때
    if cnt < 0: #예외처리
        cnt = -1
        break
    M+=5
print(cnt)
    
    
    

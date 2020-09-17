"""
11399 ATM
N명 (1<= N <= 1000)
사람당 돈을 인출하는데 걸리느 시간 P
minimum 도합 시간
"""

n = int(input())
p = list(map(int,input().split())) #list에 입력값 넣기 
p.sort() #오름차순 정렬
minTime=0
total= 0
for i in p:
    total+=i #i번째 사람에게 필요한 시간
    minTime+=total #도합시간
    
print(minTime)

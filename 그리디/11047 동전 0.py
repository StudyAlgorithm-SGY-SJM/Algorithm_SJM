"""
11047 동전 0
n: 동전 종류  (1<= n <= 10)
k원을 만드는데 필요한 동전갯수 최소값
(1<= k <=100,000,000)
동전은 오름차순으로 주어짐
"""
n, k = map(int,input().split())
coin=[]
cnt=0
for _ in range(n):
    coin.append(int(input())) #동전 종류 배열에 넣기
for i in range(n-1,-1,-1): #n-1 부터 0까지 1씩 감소
    cnt += k//coin[i]
    k=k%coin[i]
print(cnt)
    
    

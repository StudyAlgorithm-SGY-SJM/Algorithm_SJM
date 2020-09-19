"""
2217 로프
n: 로프 수 (1<= n <=100,000)
w: 중량
각 로프가 버틸수 있는 최대 중량 w/k
"""
#w/k이므로 견딜 수 있는 최대 중량이 최소인것에 맞춰야한다.
"""
minNum=10001
n = int(input())
for _ in range(n):
    minNum = min(int(input()), minNum)
print(n*minNum)
틀림................
"""
#모든 로프를 써야한다고 써있지않음!!!
#즉, 10, 1 로 주어졌을 때는 10짜리 로프로 드는것이 최대 중량
# 경우의 수를 비교해서 최댓값 도출
rope=[]
maxNum=0
n = int(input())
for _ in range(n):
    rope.append(int(input()))
rope.sort() #최대중량을 오름차순으로 정렬
for i in range(n):
    maxNum = max(maxNum, rope[i]*(n-i)) #모든 경우를 비교해서 최대인것을 저장
print(maxNum)

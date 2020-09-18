"""
1463 1로 만들기
n (1<= n <=1000000)
점화식
1은 0
1번: n은 n-1의 +1
2번: n은 n/2의 +1
3번:n은 n/3의 +1
1~3번 중 비교해서 최소를 선택
"""

n = int(input())
one = [0 for _ in range(n+1)]
for i in range(2,n+1):
    one[i]= one[i-1] +1 #1번
    if i%2 == 0: #2번
        one[i]=min(one[i],one[i//2]+1)
    if i%3 == 0: #3번
        one[i]=min(one[i],one[i//3]+1)
print(one[n])
        

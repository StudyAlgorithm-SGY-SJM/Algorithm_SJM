"""
1931 회의실 배정
n: 회의 수 (1<=n<=100,000)
회의 시간 (0<=  <=1,073,741,823)
"""
#회의시간 정렬이 제일 중요한 포인트
#끝나는 시간이 빠른 순으로 정렬되어있어야함
#끝나는 시간이 같다면 시작이간이 빠른게 앞으로 와야함 ex)[3,5],[5,5] =>2 //[5,5],[3,5] => 1
#sort함수 디테일한 사용법 잘 몰라서 구글링....

  
time=[]
n=int(input())
for _ in range(n): #input 2차원 리스트로 넣기
    s,e = map(int,input().split())
    time.append([s,e])
time.sort(key=lambda x:(x[1],x[0])) #원하는 조건으로 정렬하기
endTime=0
cnt=0 
for i, j in time:
    if endTime <= i:
        cnt+=1
        endTime = j
print(cnt)            
        

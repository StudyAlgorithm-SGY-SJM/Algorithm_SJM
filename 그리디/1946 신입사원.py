"""
1946 신입사원
선발조건: 서류성적와 면접성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자
조건을 만족하면서 선발할 수 있는 신입사원의 최대 인원수를 구하여라
t: 테스트 수(1 ≤ t ≤ 20)
n: 지원자 수(1 ≤ n ≤ 100,000)
"""
#배열에 넣고 1차테스트로 정렬 후
#i가 증가됨에 따라 2차 테스트 점수가 높은 녀석을 score값에 넣고 바꿔주며 카운트~
import sys
for _ in range(int(input())):
    applicant=[]
    n = int(sys.stdin.readline())
    for _ in range(n):
        applicant.append(list(map(int,sys.stdin.readline().split())))
   
    applicant.sort() 
    score = applicant[0][1]
    cnt=0 
    for x, y in applicant:
        if score >= y:
            score = y
            cnt+=1
    print(cnt)  

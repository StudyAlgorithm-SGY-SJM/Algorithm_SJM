"""
1541 잃어버린 괄호
+,-,0~9 길이 최대 50인 식
()를 넣어 식의 값을 최소로 만들어라
"""
#-가 나오기 전에 최대한 덧셈을 뭉친다면 최소이지 않을까?
import sys
result = 0
first = 0 #맨 앞 음수 덩어리 저장할 변수
num = sys.stdin.readline().split('-') #마이너스 기준으로 자름
for i in range(len(num)):
    arr = list(num[i].split('+')) #플러스로 나눈 수를 모두 합산
    cnt = 0
    for j in range(len(arr)):
        cnt += int(arr[j]) #합산하는 코드
        if i == 0:
            first = cnt
    result -= cnt
print(result+(first*2))

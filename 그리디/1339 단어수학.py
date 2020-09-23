'''
import sys
alpha=[-1]*26 #알파벳 개수 26개
n = int(sys.stdin.readline())
arr = [sys.stdin.readline() for _ in range(n)]
arr.sort(key=len) #길이 순으로 정렬
arr = arr[::-1] # 역순으로
lenMax=len(arr[0])
for i in range(n):
    arr[i]=arr[i].rjust(lenMax) #자릿수를 계산하기위해 공백을 넣어줌
cnt=9 #9~0 순으로 배정하기 위해
total=0
for y in range(lenMax):
    for x in range(n):
        if 'A'<= arr[x][y] <='Z' and alpha[ord(arr[x][y])-65] == -1: #중복되는 문자엔 큰자리수에있는걸 우선으로 하기위해
            alpha[ord(arr[x][y])-65]=cnt
            cnt-=1
        if 'A'<= arr[x][y] <='Z':
            total += (alpha[ord(arr[x][y])-65] * (10**(lenMax-y-2)))          
print(total)
'''
#GCF = (G*100)+(C*10)+F 이므로 alpha에 10^자릿수를 넣기로 함 
import sys
alpha=[0]*26 #알파벳 개수 26개
n = int(sys.stdin.readline())
arr = [sys.stdin.readline() for _ in range(n)]
for x in range(n):
    for y in range(len(arr[x])-1):
        alpha[ord(arr[x][y])-65] += (10**(len(arr[x])-2-y)) #자리수를 계산해서 10승한 값을 넣음
alpha.sort(reverse=True)#자릿수 큰 수부터 9~0 순으로 곱하기 위해
cnt=9 #9~0 순으로 배정하기 위해
total=0
for i in alpha:
    total+=cnt*i
    cnt-=1
print(total)

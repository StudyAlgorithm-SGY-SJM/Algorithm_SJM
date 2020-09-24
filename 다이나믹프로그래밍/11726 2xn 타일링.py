'''
점화식
s[n]=s[n-1]+s[n-2]
'''
import sys
square=[1,2]
n=int(sys.stdin.readline())
for i in range(2,n+1):
    square.append(square[i-1]+square[i-2]) 
print(square[n-1]%10007)

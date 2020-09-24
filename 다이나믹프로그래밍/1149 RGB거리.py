'''
점화식
rgb[i][0] += min(rgb[i-1][1], rgb[i-1][2])
rgb[i][1] += min(rgb[i-1][0], rgb[i-1][2])
rgb[i][2] += min(rgb[i-1][0], rgb[i-1][1])
'''

import sys
n = int(sys.stdin.readline())
rgb=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
for i in range(1,n):
    rgb[i][0] += min(rgb[i-1][1], rgb[i-1][2])
    rgb[i][1] += min(rgb[i-1][0], rgb[i-1][2])
    rgb[i][2] += min(rgb[i-1][0], rgb[i-1][1])
print(min(rgb[n-1])) # 3가지 비용중 제일 비용작은것 출력


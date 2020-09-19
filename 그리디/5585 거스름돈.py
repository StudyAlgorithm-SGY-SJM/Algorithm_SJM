"""
5585 거스름돈
so easy
"""
money = [500,100,50,10,5,1]
n = int(input())
n=1000-n
cnt=0
for i in money:
    cnt+=n//i
    n%=i
print(cnt)    

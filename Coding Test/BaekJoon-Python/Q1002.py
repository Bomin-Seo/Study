'''
이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.

조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때,
류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.
'''
from math import sqrt

ans = []
i = int(input())
for _ in range(i):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = sqrt((x1-x2)**2 + (y1-y2)**2)
    dist2 = r1 + r2
    if x1 == x2 and y1 == y2 and r1 == r2:
        ans.append(-1)
    elif dist > dist2 or dist + min(r1,r2) < max(r1,r2):
        ans.append(0)
    elif dist == dist2:
        ans.append(1)
    else:
        ans.append(2)

for i in range(len(ans)):
    print(ans[i])
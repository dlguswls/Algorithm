### 크로스 컨트리 ###
# 한 팀은 6명의 선수, 상위 네 명의 점수 합산, 가장 낮은 점수 우승
# 자격을 갖춘 팀에만 점수 부여
# 점수는 결승점 통과 순서
# 동점의 경우 다섯 번째 주자 고려

# import sys

# T = int(sys.stdin.readline().strip()) # Test Case 개수
# for _ in range(T) : 
#     N = int(sys.stdin.readline().strip()) # 주자 수
#     teams = sys.stdin.readline().strip().split()
#     Team = set(teams)

#     # 조건 안되는 팀 없애기
#     for i in Team : 
#         cnt = teams.count(i)
#         if cnt < 6 : 
#             for j in range(cnt) : 
#                 teams.remove(i)
#     Team = set(teams)

#     # 팀별 점수 부여하기
#     score = [i+1 for i in range(len(teams))]
#     score_dict = {}
#     for i in Team : 
#         score_dict[i] = []

#     cnt = 0
#     for i in teams : 
#         score_dict[i].append(score[cnt])
#         cnt += 1
   
#     score_result = {}
#     for i in Team : 
#         score_result[i] = []
#         score_result[i].append(sum(score_dict[i][:4]))
#         score_result[i].append(sum(score_dict[i][:5]))
#     score_result = dict(sorted(score_result.items(), key = lambda x : (x[1][0], x[1][1])))
#     print(list(score_result.keys())[0])



#### 다른 풀이 ####
import sys
from collections import Counter

T = int(sys.stdin.readline().strip()) # Test Case 개수
for _ in range(T) : 
    N = int(sys.stdin.readline().strip()) # 주자 수
    teams = sys.stdin.readline().strip().split()
    count = Counter(teams)
    out = 0
    result = {}
    for i in range(N) : 
        if count[teams[i]] < 6 : 
            out += 1
            continue
        if teams[i] in result : 
            result[teams[i]].append(i-out)
        else : 
            result[teams[i]] = [i-out]
    # print(sorted(result, key = lambda x : (sum(result[x][:4]), result[x][4]))[0])
    print(sorted(result.items(), key = lambda x : (sum(x[1][:4]), x[1][4]))[0][0])

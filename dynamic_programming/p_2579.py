# p 2579
# 계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다.
# <그림 1>과 같이 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.

def get_max_score(acc_scores, preprev_step, prepreprev_step, prev_step_score):
    if acc_scores[preprev_step] > acc_scores[prepreprev_step] + prev_step_score:
        return acc_scores[preprev_step]
    else:
        return acc_scores[prepreprev_step] + prev_step_score

num_stair = int(input())
score_stair = []

for i in range(num_stair):
    score_stair.append(int(input()))

acc_scores = [0, score_stair[0],
              score_stair[0] + score_stair[1]]

for i in range(3,num_stair+1):
    temp_score = get_max_score(acc_scores,i-2, i-3, score_stair[i-2])
    acc_scores.append(temp_score + score_stair[i-1])


print(acc_scores[-1])

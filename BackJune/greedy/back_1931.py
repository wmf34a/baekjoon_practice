import sys
input = sys.stdin.readline

def main():
    N = int(input())
    meeting = []
    for _ in range(N):
        start_time, end_time = map(int, input().split())
        meeting.append((start_time,end_time))

    a = sorted(meeting, key=lambda x : (x[1], x[0]))
    meeting_cnt, start_time = 0,0
    for j in a:
        if j[0] >= start_time:
            start_time = j[1]
            meeting_cnt +=1
    print(meeting_cnt)
# 회의 가능 시간(1, 4) (5, 7) (8, 11) (12, 14)
main()


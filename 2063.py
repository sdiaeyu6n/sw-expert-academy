T = int(input())
score_list=list(map(int, input().split()))
score_list.sort()
print(score_list[T//2])
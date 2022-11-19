T=int(input())
result=[]
for tc in range(T):
    N, M = map(int, input().split())
    square = []
    target = [[0 for i in range(M)] for j in range(M)]

    for i in range(N):
        square.append(list(map(int, input().split())))
    dead_fly = 0
    for l in range(N - M+1):
        for k in range(N - M+1):
            for i in range(M):
                for j in range(M):
                    target[i][j] = square[l+i][k+j]
            temp = 0
            for t in target:
                temp += sum(t)
            if temp > dead_fly:
                dead_fly = temp

    result.append(dead_fly)
for i in range(T):
    print(f"#{i+1}",result[i])
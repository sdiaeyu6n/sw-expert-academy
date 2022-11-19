T = int(input())
test_case=[]
for i in range(T):

    N = int(input())
    # 방향: 우->하->좌->상
    dir_row = [0, 1, 0, -1]
    dir_col = [1, 0, -1, 0]
    snail = [[0 for j in range(N)] for i in range(N)]

    r = 0
    c = 0
    dist = 0  # 0:우, 1:하, 2:좌, 3:상
    for num in range(1, N * N + 1):

        snail[r][c] = num

        r += dir_row[dist]
        c += dir_col[dist]

        if r > N - 1 or c > N - 1 or snail[r][c] != 0:
            r -= dir_row[dist]
            c -= dir_col[dist]
            dist = (dist + 1) % 4
            r += dir_row[dist]
            c += dir_col[dist]
    test_case.append(snail)

i=0
for tc in test_case:
    print("#"+str(i+1))
    i+=1
    for s in tc:
        print(*s)
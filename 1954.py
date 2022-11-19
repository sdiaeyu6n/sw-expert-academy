T = int(input())
test_case=[]
for i in range(T):

    N = int(input())
    # 인덱스를 활용해서 방향전환을 하고 싶을때는 
    # delta row(dr), delta column(dc) 리스트를 만들고 접근하면 된다

    # 방향: 우->하->좌->상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    snail = [[0 for j in range(N)] for i in range(N)]

    r = 0
    c = 0
    dist = 0  # 0:우, 1:하, 2:좌, 3:상
    for num in range(1, N * N + 1):

        snail[r][c] = num

        r += dr[dist]
        c += dc[dist]

        if r > N - 1 or c > N - 1 or snail[r][c] != 0:
            # 인덱스 원위치
            r -= dr[dist]
            c -= dc[dist]
            # dist를 0,1,2,3 내의 값으로 유지
            dist = (dist + 1) % 4
            # 방향 전환 (dist+1)
            r += dr[dist]
            c += dc[dist]
    test_case.append(snail)

i=0
for tc in test_case:
    print("#"+str(i+1))
    i+=1
    for s in tc:
        print(*s)
T = int(input())

for i in range(T):
    N = int(input())
    triangle = [[1]*n for n in range(1,N+1)]

    for m in range(2,N): # 층
        for k in range(1,m): # 호
            triangle[m][k]=triangle[m-1][k-1]+triangle[m-1][k]

    print(f"#{i+1}")
    for num in triangle:
        print(" ".join(map(str,num)))
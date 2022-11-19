T = int(input())
test_case=[]
for i in range(T):
    N=int(input())
    result=0
    for i in range(1,N+1):
        if i%2==0:
            result-=i
        else:
            result+=i
    test_case.append(result)

for i in range(T):
    print(f"#{i+1}",test_case[i])
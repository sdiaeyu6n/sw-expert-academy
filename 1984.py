T = int(input())
test_case=[]
for i in range(T):
    num_list=list(map(int,input().split()))
    num_list.remove(max(num_list))
    num_list.remove(min(num_list))
    test_case.append(round(sum(num_list)/8))

for i in range(T):
    print(f"#{i+1}",test_case[i])
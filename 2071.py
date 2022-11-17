T=int(input())
test_list=[]
for i in range(T):
    test_list.append(list(map(int,input().split())))

avg_list=[]
for i in range(T):
    print("#"+str(i+1),round(sum(test_list[i])/10))
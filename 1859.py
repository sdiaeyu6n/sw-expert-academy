T = int(input())
profit_list = []
for i in range(T):
    buy = 0
    count = 0
    profit = 0
    N = int(input())
    case = list(map(int, input().split()))
    case.reverse()
    while len(case)>0:
        max_num = max(case)
        if case[-1]!=max_num:
            buy+=case.pop()
            count+=1
        else:
            profit+=case.pop()*count-buy
            count = 0
            buy=0
    profit_list.append("#"+str(i+1)+" "+str(profit))

for pf in profit_list:
    print(pf)
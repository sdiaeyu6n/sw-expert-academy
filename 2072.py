T=int(input())
sum_result=[]
for i in range(1,T+1):
    num_list=list(map(int,input().split()))
    sum=0
    for num in num_list:
        if num%2!=0:
            sum+=num
        else:
            continue
    result="#"+str(i)+" "+str(sum)
    sum_result.append(result)

for s in sum_result:
    print(s)
N=int(input())
result=['' for i in range(N)]

for i in range(0,N):
    count = 0
    num=list(str(i+1))
    for j in num:
        if j == '3' or j=='6' or j=='9':
            count+=1
    if count!=0:
        result[i]='-'*count
    else: result[i]=str(i+1)
print(' '.join(result))
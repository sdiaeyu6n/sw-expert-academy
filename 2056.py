T = int(input())
result=[]
for i in range(T):
    case = list((input()))
    case_year = case[0] + case[1] + case[2] + case[3]
    case_month = case[4] + case[5]
    case_day = case[6] + case[7]

    if case_month in ['01', '03', '05', '07', '08', '10', '12'] \
            and 1 <= int(case_day) <= 31:
        result.append("#"+str(i+1)+" "+case_year+"/"+case_month+"/"+case_day)
    elif case_month == '02' and 1 <= int(case_day) <= 28:
        result.append("#"+str(i+1)+" "+case_year+"/"+case_month+"/"+case_day)
    elif case_month in ['04', '06', '09', '11'] \
            and 1 <= int(case_day) <= 30:
        result.append("#"+str(i+1)+" "+case_year+"/"+case_month+"/"+case_day)
    else: result.append("#"+str(i+1)+" "+'-1')

for date in result:
    print(date)
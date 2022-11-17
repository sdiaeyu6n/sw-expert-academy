T = int(input())
result = []
for i in range(T):
    case = list(input())
    print(len(case))
    for j in range(len(case)):
        result.append(case[j])
        print(result[:len(result)//2])
        print("=========")
        print(result[len(result)//2:])
        if result[:j] == result[j:]:
            print(result)
            break
            # print(result)
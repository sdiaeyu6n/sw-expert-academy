T = int(input())
test_list = []
for i in range(T):
    test_list.append(list(map(int, input().split())))
for i in range(T):
    print("#" + str(i + 1), max(test_list[i]))
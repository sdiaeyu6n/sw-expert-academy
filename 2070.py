T = int(input())
test_list = []
for i in range(T):
    test_list.append(list(map(int, input().split())))
for i in range(T):
    if test_list[i][0] > test_list[i][1]:
        print("#" + str(i + 1), ">")
    elif test_list[i][0] < test_list[i][1]:
        print("#" + str(i + 1), "<")
    else:
        print("#" + str(i + 1), "=")
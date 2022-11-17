str_input=list(input())
converted_list=[]
for alp in str_input:
    converted_list.append(ord(alp)-64)

print(" ".join(map(str,converted_list)))
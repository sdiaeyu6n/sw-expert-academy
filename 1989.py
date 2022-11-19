T=int(input())
result=[]
for i in range(T):
    word=input()
    reversed_word="".join(reversed(word))
    if word == reversed_word:
        result.append(1)
    else:
        result.append(0)

for i in range(T):
    print(f"#{i+1}",result[i])
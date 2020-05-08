word_list = input().split()
op_list = list()
op_list.append(word_list[0])
for word in word_list[1:]:
    op_list.append(word.title())
if len(op_list) == 1:
    print(op_list[0])
else:
    print("".join(op_list))
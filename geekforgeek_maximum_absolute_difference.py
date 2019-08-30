def pick_max(l):
    return l.index(max(l))

for _ in range(int(input())):
    n = int(input())
    list_input = list(map(int, input().split()))
    temp_list = [0] * n
    while len(list_input) > 0:
        max_index = pick_max(list_input)
        if max_index == 0 and len(list_input) == 1:
            temp_list[max_index] = list_input[max_index]
            del list_input[max_index]    
        elif max_index == len(list_input) - 1:
            temp_list[max_index - 1] = 1
            temp_list[max_index] = list_input[max_index]
            del list_input[max_index]
            del list_input[max_index - 1]
        elif max_index == 0:
            temp_list[max_index + 1] = 1
            temp_list[max_index] = list_input[max_index]
            del list_input[max_index + 1]
            del list_input[max_index]
        else:
            temp_list[max_index - 1] = 1
            temp_list[max_index] = list_input[max_index]
            temp_list[max_index + 1] = 1
            del list_input[max_index + 1]
            del list_input[max_index]
            del list_input[max_index - 1]
    l = []
    for i in range(len(temp_list) - 1):
        l.append(abs(temp_list[i] - temp_list[i + 1]))
    print(sum(l))    

li_1, li_2 = ([int(num) for num in input().split()] for _ in range(2))

msg = 'нет'

for i in range(len(li_1) - len(li_2)):
    if not li_2:
        msg = 'да'
        break
    check = 0
    if li_1[i] == li_2[0]:
        for j in range(len(li_2)):
            if li_1[i + j] == li_2[j]:
                check += 1
        if check == len(li_2):
            msg = 'да'
            break
        
print(msg)


# 1
# 
# да

# 1 2 3 4
# 2 3
# да

# 1 2 3 4
# 2 4
# нет

# 1 2 3 4 0 1 2 4 3
# 0 1 2
# да

# 0 1 2 3 0 1 3 0 1 3
# 1 3
# да
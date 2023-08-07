string = input() 

true_set = not len(set(string) - {'b', '0', '1'})
true_prefix = string[:2] == '0b' or string[:1] == 'b' or 'b' not in string

message = 'да' if true_set and true_prefix else 'нет'

print(message)

# 10111
# да

# b1011101
# да

# 0b1011101
# да

# 10222
# нет

# b10222
# нет

# 1b10111
# нет

# 2b101011
# нет
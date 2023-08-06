my_dict = dict()

while inp := input(' item > '):
    my_dict[int(inp.split()[0])] = inp.split()[1]

find_val = input(' find > ')
show_msg = '! value error !'
for key, value in my_dict.items():   
    if find_val == value:
        show_msg = key
        break
        
print(' msg ', show_msg)


# item > 1 er1
# item > 2 er2
# item > 3 er3
# item > 4 er4
# item >
# find > er5
# msg  ! value error !

# item > 1 er1
# item > 2 er2
# item > 3 er3
# item > 4 er4
# item >
# find > er4
# msg  4

# item > 1004 ER_CANT_CREATE_FILE
# item > 1005 ER_CANT_CREATE_TABLE
# item > 1006 ER_CANT_CREATE_DB
# item > 1007 ER_DB_CREATE_EXISTS
# item > 1008 ER_DB_DROP_EXISTS
# item > 1010 ER_DB_DROP_RMDIR
# item > 1016 ER_CANT_OPEN_FILE
# item > 1022 ER_DUP_KEY
# item >
# find > ER_CANT_CREATE_DB
# msg  1006

# item > 1004 ER_CANT_CREATE_FILE
# item > 1005 ER_CANT_CREATE_TABLE
# item > 1007 ER_DB_CREATE_EXISTS
# item > 1008 ER_DB_DROP_EXISTS
# item > 1010 ER_DB_DROP_RMDIR
# item > 1016 ER_CANT_OPEN_FILE
# item > 1022 ER_DUP_KEY
# item >
# find > ER_CANT_CREATE_DB
# msg  ! value error !
files_list = sorted(input().split('; '))
files_data = {file: files_list.count(file) for file in files_list}
files_save = list()

for key, value in files_data.items():
    files_save.append(key)
    # КОММЕНТАРИЙ: хорошо, что обошлись range(), без явных проверок значения value
    # ПЕРЕИМЕНОВАТЬ: счётчик — counter, cnt
    for counter in range(2, value+1):
        # ИСПОЛЬЗОВАТЬ: оптимизацию количества операций со строками
        i_dot = key.index(".")
        files_save.append(f'{key[:i_dot]}_{counter}{key[i_dot:]}')
    
print(*files_save, sep='\n')


# 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.py; src.tar.gz
# 1.py
# 1_2.py
# 1_3.py
# aux.h
# functions.h
# main.cpp
# main_2.cpp
# main.py
# src.tar.gz
# src_2.tar.gz

# 1.py; 1.py; 1.py; 1.txt; 1.txt; index.html; index.html; img.jpeg; img.png; img.jpeg
# 1.py
# 1_2.py
# 1_3.py
# 1.txt
# 1_2.txt
# img.jpeg
# img_2.jpeg
# img.png
# index.html
# index_2.html


# ИТОГ: очень хорошо — 5/6

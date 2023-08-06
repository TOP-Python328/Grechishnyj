# files_str = '1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.py; src.tar.gz'

files_list = sorted(input().split('; '))
files_data = {file:files_list.count(file) for file in files_list}
files_save = list()

for key, value in files_data.items():
    files_save.append(key)
    for i in range(2, value + 1):
        files_save.append(f'{key[:key.index(".")]}_{i}{key[key.index("."):]}')
    
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
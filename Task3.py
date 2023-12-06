file_dict = {}
file_name1 = "1.txt"
file_name2 = "2.txt"
file_name3 = "3.txt"
with open(file_name1, encoding='utf-8') as fil1:
    file_dict[file_name1] = fil1.readlines()
with open(file_name2, encoding='utf-8') as fil2:
    file_dict[file_name2] = fil2.readlines()
with open(file_name3, encoding='utf-8') as fil3:
    file_dict[file_name3] = fil3.readlines()
str_to_write = ""
last_file = ""
min_len = min(len(file_dict[file_name1]), len(file_dict[file_name2]), len(file_dict[file_name3]))
if min_len == len(file_dict[file_name1]):
    str_to_write += f"{file_name1}\n{len(file_dict[file_name1])}\n{''.join(file_dict[file_name1])}\n"
    min_len2 = min(len(file_dict[file_name2]), len(file_dict[file_name3]))
    if min_len2 == len(file_dict[file_name2]):
        str_to_write += f"{file_name2}\n{len(file_dict[file_name2])}\n{''.join(file_dict[file_name2])}\n"
        last_file = file_name3
    else:
        str_to_write += f"{file_name3}\n{len(file_dict[file_name3])}\n{''.join(file_dict[file_name3])}\n"
        last_file = file_name2    
elif min_len == len(file_dict[file_name2]):
    str_to_write += f"{file_name2}\n{len(file_dict[file_name2])}\n{''.join(file_dict[file_name2])}\n"
    min_len2 = min(len(file_dict[file_name1]), len(file_dict[file_name3]))
    if min_len2 == len(file_dict[file_name1]):
        str_to_write += f"{file_name1}\n{len(file_dict[file_name1])}\n{''.join(file_dict[file_name1])}\n"
        last_file = file_name3
    else:
        str_to_write += f"{file_name3}\n{len(file_dict[file_name3])}\n{''.join(file_dict[file_name3])}\n"
        last_file = file_name1
else:
    str_to_write += f"{file_name3}\n{len(file_dict[file_name3])}\n{''.join(file_dict[file_name3])}\n"
    min_len2 = min(len(file_dict[file_name1]), len(file_dict[file_name2]))
    if min_len2 == len(file_dict[file_name1]):
        str_to_write += f"{file_name1}\n{len(file_dict[file_name1])}\n{''.join(file_dict[file_name1])}\n"
        last_file = file_name2
    else:
        str_to_write += f"{file_name2}\n{len(file_dict[file_name2])}\n{''.join(file_dict[file_name2])}\n"
        last_file = file_name1
str_to_write += f"{last_file}\n{len(file_dict[last_file])}\n{''.join(file_dict[last_file])}\n"
print(str_to_write)
with open('4.txt', "w", encoding='utf-8') as fil4:
    fil4.write(str_to_write)
cook_book = {}
with open('recipes.txt', encoding='utf-8') as fil:
    data_lines = fil.readlines()
    next_ = False
    for line_str in data_lines:
        if line_str.find("|") == -1 and len(line_str.rstrip()) >= 2:
           next_ = True
        if next_:
            dish = line_str.rstrip()
            cook_book[dish] = []
        next_ = False
        if line_str.find("|") != -1:
            st = line_str.rstrip()
            inrid_list = st.split(" | ", 3)
            dish_dict = {}
            dish_dict["ingredient_name"] = inrid_list[0] 
            dish_dict["quantity"] = inrid_list[1]
            dish_dict["measure"] = inrid_list[2]
            cook_book[dish] += [dish_dict]
print(cook_book)       
        
mixed_1=["red", "green", "blue", "yellow"]
mixed_2=[1, 20, 30, 40, 100]

for item in mixed_list:
    if isinstance(item,(int,float)):
        mixed_1.append(item)
    else:
        mixed_2.append(item)
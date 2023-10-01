listData = [0, 15, 31, 69, -888]
max = listData[0]

for i in listData:
    if i > max:
        max = i

txt = "The maximum is {} "
print(txt.format(max))
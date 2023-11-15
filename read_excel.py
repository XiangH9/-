import pandas as pd
homework_path=input("提交作业目录:")
excel_file_path=input("班级名单目录:")
# excel_file_path="D:\大三上学期\工程实践创新中心\list.xlsx"
df=pd.read_excel(excel_file_path)


row_num=1  # 一般第二列是姓名
# 这里比较弱智的是需要我们手动调节至含有姓名的那一列
list_name=df.iloc[:,row_num]

# print("姓名：")
# print(list_name)


import os
# homework_path="D:\大三上学期\工程实践创新中心\homework"
file_names=os.listdir(homework_path)
# print(file_names)

not_name=[]
for i in range(len(list_name)):
    name=list_name[i]
    # print("name:")
    # print(name)
    k=0
    for j in file_names:
        # print(j)
        if name not in j:
            k=k+1
    if k == len(file_names):
        not_name.append(name)
print("未交作业名单:")
print(not_name)

import pandas as pd
from pandas import DataFrame

'''
# 查看所有的值
print(excel_1.values)
# 查看第一行的值
print(excel_1.values[0])
# 查看某一列所有的值
print(excel_3['指标'].values)

#新增列
excel_1['标题列3'] = None
#新增行
excel_1.loc[3] = ['王五', 100, '男']
#删除行：axis=0
data = excel_1.drop([0,1], axis=0)
#删除列：axis=1
data.drop('标题列3', axis=1)
# 保存
DataFrame(excel_1).to_excel('1.xlsx', sheet_name='Sheet1', index=False, header=True)
'''

filename_read = "./拜博管报切换-新.xlsx" #源文件
filename_result = './Result.xlsx'#输出文件

excel_1 = pd.read_excel(filename_read,sheet_name='新管报', dtype=str,keep_default_na=False)
excel_3 = pd.read_excel(filename_read,sheet_name='最终报表-A表', dtype=str,keep_default_na=False)

def find_loc(values,findstr):
    for i in range(len(values)):
        for j in range(len(values[0])):
            if findstr == values[i][j]:
                return (i,j) # 第i行，第j列

    return None


col_TKI_all = excel_1.values

col1 = excel_3['展示名称'].values
col2 = excel_3['代码-管报'].values
col_all = excel_3.values

for i in range(len(col1)):
    loc = find_loc(col_TKI_all,col1[i].strip('* '))
    if loc:
        col2[i] = col_TKI_all[loc[0]][loc[1] - 1]
        print(col1[i], col2[i])
    else:
        print(col1[i], col2[i])


for i in  range(len(col1)):
    col_all[i][2] = col2[i]
    print(col1[i],col2[i])


DataFrame(col_all).to_excel(filename_result, sheet_name='Sheet1', index=False, header=True)



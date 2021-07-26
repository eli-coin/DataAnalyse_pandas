#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:eli
@file:筛选.py
@time:2021/07/26
在csv文件中的某些列中，查找包含指定关键字的行
"""
import pandas as pd
filename_read = "info.csv" #源文件
filename_result = 'Result.csv'#输出文件
KEYS = ["网络", "计算机", "软件", "信息"]#筛选根据关键字
COLUMNS = ['第一学历专业', '最高学历专业']#需要筛选的列


csv_read = pd.read_csv(filename_read, sep=',', encoding="UTF-8",dtype=str,keep_default_na=False)
"""
sep,分隔符
dtype,读取数据type
keep_default_na,读取到空字符串时读出的是''而不是nan()
"""
##############一行代码实现筛选###################
# data_csv_tmp = csv_read[(csv_read['第一学历专业'].str.contains('网络')) | (csv_read['最高学历专业'].str.contains('网络'))\
#     | (csv_read['第一学历专业'].str.contains('计算机')) | (csv_read['最高学历专业'].str.contains('计算机'))\
#     | (csv_read['第一学历专业'].str.contains('软件')) | (csv_read['最高学历专业'].str.contains('软件'))\
#     | (csv_read['第一学历专业'].str.contains('信息')) | (csv_read['最高学历专业'].str.contains('信息'))]
# data_csv_tmp.to_csv(filename_result,encoding="UTF-8")
##############一行代码实现筛选###################

# 打印
def print_csv(data_csv, col_start=0, col_end=0):
    if col_end == 0:
        print(data_csv.head())
    else:
        print(data_csv[col_start:col_end])


# 获取dataFrame的行or列数
def get_col_row(data_csv, mode="col"):
    if mode == 'col':
        return int(data_csv.shape[0])  # 行数
    elif mode == 'row':
        return int(data_csv.shape[0])  # 列数
    else:
        print("错误！", "get_col_row函数，仅接受参数——col或者row")
        return False


# 判断column是否存在key
def haskey(column:str):
    for key in KEYS:
        if key in column:
            return True
    return False

def go():
    SUM_CLOS = 0
    for i in range(get_col_row(csv_read, mode="col")):
        column = "" #存储需要筛选的列内容
        for col in COLUMNS:
            column += str(csv_read.loc[i,col])
        # TAG1 = csv_read.iloc[i, 0] # 按照数字定位
        # TAG1 = str(csv_read.loc[i, '专业']) #按照表头定位
        if haskey(column):
            data_csv_tmp = csv_read.iloc[[i]] # 抽取第i行数据，写入文件
            if SUM_CLOS == 0:
                data_csv_tmp.to_csv(filename_result, index=None, mode='a', encoding="UTF-8")
            else:
                data_csv_tmp.to_csv(filename_result,index=None,mode="a",encoding="UTF-8",header=None) # 第一条数据插入表头
            SUM_CLOS += 1
        else:
            pass
    print("finished! 符合条件的记录数目:", SUM_CLOS)


if __name__ == '__main__':
    go()
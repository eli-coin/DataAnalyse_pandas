import pandas as pd

filer1 = "file1.csv"
filer2 = "file2.csv"
res_file = "抽样结果.csv"

csv_read1 = pd.read_csv(filer1,sep=",",encoding="GBK",keep_default_na=False)
csv_read2 = pd.read_csv(filer2,sep=",",encoding="GBK",keep_default_na=False)

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

# 四舍五入
def to_int(NUMS):
    nInt = int(NUMS)
    return nInt if (NUMS-nInt) <0.5 else (nInt+1)

# 按照参数获取一类数据
def get_one_type(col1,col2,col3):
    data_csv_tmp = csv_read2[(csv_read2['col1'] == col1) &
                             (csv_read2['col2'] == col2) &
                             (csv_read2['col3'] == col3)]
    return data_csv_tmp

# 抽样主函数
def chouyang():
    SUM = 0
    choose_count_sum = get_col_row(csv_read1)
    for i in range(choose_count_sum):
        col1 = csv_read1.loc[i, 'col1']
        col2 = csv_read1.loc[i, 'col2']
        col3 = csv_read1.loc[i, 'col3']
        # col4 = csv_read1.loc[i, 'col4'] # 用不到的参数
        col5 = csv_read1.loc[i, 'col5']
        NUMS = to_int(col5) # 四舍五入，获取抽样数据条数

        data_csv_tmp = get_one_type(col1,col2,col3)
        csv_tmp = data_csv_tmp.sample(n=NUMS)
        if i != 0:
            csv_tmp.to_csv(res_file, index=None, mode='a', encoding="GBK", header=None) # 不输出表头
        else:
            csv_tmp.to_csv(res_file, index=None, mode='a', encoding="GBK") # 输出表头
        print("随机抽样:{},{},{},{},".format(col1,col2,col3,NUMS))
        SUM += NUMS


    print("总共抽样：",SUM)




if __name__ == '__main__':
    chouyang()
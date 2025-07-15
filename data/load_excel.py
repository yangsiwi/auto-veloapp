import pandas


# 读取excel的数据  做为数据来源去进行测试
# 读取excel的数据  openpyxl\pandas
# 安装  pip install pandas -i  镜像
# 报错openpyxl（安装）

# 目的：为了把excel数据读取出来，给到测试用例使用
def pandas_read_excel_dict(filename,sheetname):
    # 读取excel数据  excel数据在哪 表单名称
    data=pandas.read_excel(filename,sheet_name=sheetname)
    print("excel中的数据", data)
    # 用空字符填充数据中的Nan
    data=data.where(data.notnull(),'')
    print("excel中处理为空的数据", data)
    # 转成字典格式  列表嵌套了字典
    datadict=data.to_dict(orient='records')
    print("转成字典数据", datadict)
    # datalist = data.values.tolist()
    # print("转成列表数据", datalist)
    return datadict

if __name__ == '__main__':
    pandas_read_excel_dict("velotric.xlsx",'Sheet1')
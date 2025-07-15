import os

import pytest
from allure_combine import combine_allure

args = [
    '-vs',  # 日志信息更详细
    '--capture=sys',  # 会在allure报告中展示 stdout 的小文本
    '--clean-alluredir',  # 清空数据每次获得的是最新的数据
    '--alluredir=allure-results',  # 生成测试数据，数据放在allure-results文件夹里面
    # r'/Users/wayne/Documents/work/auto-veloapp/test_case/test_login.py'
]

pytest.main(args)

# 生成报告  生成在allure-report文件夹中
os.system("allure generate -c -o allure-report")
# os.system("allure generate ./allure-results -o ./allure-report --clean")


combine_allure('allure-report')

# pom执行过程
# 1.开始执行用例cli.py;指定用例或者不指定 符合 pytest 规则的用例都执行;
# 2.在执行 conftest 里面的 fixture 内容，yield 前面内容先执行 再执行用例 再执行 yield 之后的事情;
# 3.在执行用例的时候 数据来源是来源 yaml 文件，用参数化把数据传到用例中去;
# 4.调用登录页面的方式，你还得传个设备信息给 Keywords 父类;

# pom没有固定的写法 只要是你觉得方便合适就可以按照你的思维写法

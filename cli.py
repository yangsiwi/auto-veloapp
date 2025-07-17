# import os
# import pytest
# from allure_combine import combine_allure
#
# args = [
#     '-vs',  # 日志信息更详细
#     '--capture=sys',  # 会在allure报告中展示 stdout 的小文本
#     '--clean-alluredir',  # 清空数据每次获得的是最新的数据
#     '--alluredir=allure-results',  # 生成测试数据，数据放在allure-results文件夹里面
#     # r'/Users/wayne/Documents/work/auto-veloapp/test_case/test_login.py'
# ]
#
# pytest.main(args)
#
# # 生成报告  生成在allure-report文件夹中
# os.system("allure generate -c -o allure-report")
# # os.system("allure generate ./allure-results -o ./allure-report --clean")
#
#
# combine_allure('allure-report')
#
# # pom执行过程
# # 1.开始执行用例 cli.py 指定用例或者不指定，符合 pytest 规则的用例都执行。
# # 2.再执行 conftest 里面的 fixture 内容，yield 前面内容先执行，再执行用例，再执行 yield 之后的事情。
# # 3.在执行用例的时候，数据来源是 yaml 文件，用参数化把数据传到用例中去。
# # 4.调用登录页面的方式，你还得传个设备信息给 Keywords 父类。
#
# # pom没有固定的写法 只要是你觉得方便合适就可以按照你的思维写。


#
# import os
# import pytest
# from allure_combine import combine_allure
#
# args = [
#     '-vs',  # 日志信息更详细
#     '--capture=sys',  # 会在allure报告中展示 stdout 的小文本
#     '--clean-alluredir',  # 清空数据每次获得的是最新的数据
#     '--alluredir=allure-results',  # 生成测试数据，数据放在allure-results文件夹里面
#     # r'/Users/wayne/Documents/work/auto-veloapp/test_case/test_login.py'
# ]
#
# pytest.main(args)
#
# # 生成报告  生成在allure-report文件夹中
# os.system("allure generate -c -o allure-report")
# # os.system("allure generate ./allure-results -o ./allure-report --clean")
#
#
# combine_allure('allure-report')

# pom执行过程
# 1.开始执行用例 cli.py 指定用例或者不指定，符合 pytest 规则的用例都执行。
# 2.再执行 conftest 里面的 fixture 内容，yield 前面内容先执行，再执行用例，再执行 yield 之后的事情。
# 3.在执行用例的时候，数据来源是 yaml 文件，用参数化把数据传到用例中去。
# 4.调用登录页面的方式，你还得传个设备信息给 Keywords 父类。

# pom没有固定的写法 只要是你觉得方便合适就可以按照你的思维写。


import pytest
import argparse
import subprocess
from allure_combine import combine_allure


def run_tests(pytest_args):
    """封装测试执行和报告生成"""

    # 基础参数
    base_args = [
        '-vs',
        '--capture=sys',
        '--clean-alluredir',
        '--alluredir=allure-results',
    ]

    # 合并基础参数和从命令行传入的额外参数
    final_args = base_args + pytest_args
    print(f"执行Pytest，参数: {final_args}")

    # 执行测试
    pytest.main(final_args)

    # 【优化】使用 subprocess 替代 os.system，更安全、更灵活
    print("生成Allure报告...")
    generate_command = "allure generate allure-results -o allure-report --clean"

    # 执行命令，并检查执行结果
    result = subprocess.run(generate_command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        print("Allure报告生成成功。")
        combine_allure('allure-report') # 如果需要合并报告，保留此行
    else:
        print("Allure报告生成失败！")
        print("错误信息:", result.stderr)


if __name__ == "__main__":
    # --- 使用 argparse 解析命令行参数 ---
    parser = argparse.ArgumentParser(description="Velotric App自动化测试运行器")

    # 添加 -k 参数，用于按关键字/名称运行测试 (例如: -k test_login)
    parser.add_argument('-k', '--keyword', type=str, help='按关键字运行匹配的测试用例。')

    # 添加 -m 参数，用于按标记运行测试 (例如: -m smoke)
    parser.add_argument('-m', '--marker', type=str, help='运行带有特定标记的测试用例。')

    # 添加 --path 参数，用于指定要运行的测试文件或目录
    parser.add_argument('--path', type=str, default='.', help='指定要运行的测试文件或目录，默认为当前目录。')

    args = parser.parse_args()

    # --- 组装 pytest 参数 ---
    extra_pytest_args = []
    if args.keyword:
        extra_pytest_args.extend(['-k', args.keyword])
    if args.marker:
        extra_pytest_args.extend(['-m', args.marker])

    # 将测试路径作为最后一个参数
    extra_pytest_args.append(args.path)

    # 运行测试
    run_tests(extra_pytest_args)


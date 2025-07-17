import pytest
import argparse
import subprocess
from allure_combine import combine_allure

"""
定义一个名为 run_tests 的函数，它接收一个参数 pytest_args。
我们期望这个参数是一个列表，包含了要传递给Pytest的额外指令。
"""


def run_tests(pytest_args):
    """封装 测试执行 和 报告生成 """

    # 基础参数
    """
    创建一个名为 base_args 的列表。
    这里存放的是每次运行都固定不变的Pytest基础参数。
    """
    base_args = [
        '-vs',  # Verbose (详细) 模式，输出更详细的测试执行信息。Show prints (显示打印)，在测试结果中显示代码里的 print() 输出。
        '--capture=sys',  # 配合 -s，确保标准输出能被正确捕获并显示。
        '--clean-alluredir',  # 在运行前，清空上一次生成的Allure结果目录（allure-results），确保每次报告都是最新的。
        '--alluredir=allure-results',  # 指定Allure的原始测试结果（通常是一些JSON文件）要存放在名为 allure-results 的文件夹里。
    ]

    # 合并基础参数和从命令行传入的额外参数
    """
    将固定的 base_args 和从外面传进来的 pytest_args。
    两个列表合并成一个最终的参数列表 final_args。
    """
    final_args = base_args + pytest_args
    print(f"执行Pytest，参数: {final_args}")

    # 执行测试
    """
    用 pytest.main() 函数，并把我们精心组装好的 final_args 列表传给它。
    Pytest就会按照这个列表里的指令开始查找和执行测试用例。
    """
    pytest.main(final_args)

    # 【优化】使用 subprocess 替代 os.system，更安全、更灵活
    print("生成Allure报告...")
    """
    定义一个字符串，内容就是我们在命令行里手动生成报告时敲的命令。
    allure generate: 调用Allure的生成报告命令。
    allure-results: 指定原始数据来源的目录。
    -o allure-report: Output (输出) 到名为 allure-report 的目录。
    --clean: 在生成新报告前，清空上一次的 allure-report 目录。
    """
    generate_command = "allure generate allure-results -o allure-report --clean"

    # 执行命令，并检查执行结果
    """
    使用 subprocess.run() 来执行上面定义的 generate_command 命令。
    shell=True: 表示这条命令需要通过系统的 shell (比如Windows的cmd, Linux的bash) 来解释执行。对于包含管道、重定向等复杂语法的命令，通常需要它。
    capture_output=True: 告诉 subprocess：“请帮我捕获这个命令在执行过程中的所有标准输出和标准错误输出。”
    text=True: 让捕获到的输出以文本（字符串）格式存储，而不是二进制格式，方便我们阅读。
    行完毕后会返回一个对象，里面包含了这次命令执行的所有信息（是否成功、输出内容、错误内容等），我们把它存到 result 变量里。
    """
    result = subprocess.run(generate_command, shell=True, capture_output=True, text=True)

    """
    检查 `result` 对象的 `returncode` (返回码)。
    在命令行世界里，返回码 `0` 通常代表“成功”，任何非零值都代表“失败”。
    """
    if result.returncode == 0:
        """如果成功，打印成功信息，并调用 `combine_allure` 函数去执行合并报告的操作。"""
        print("Allure报告生成成功。")
        combine_allure('allure-report')  # 如果需要合并报告，保留此行
    else:
        """
        如果失败，打印失败信息，并把 `result.stderr` (标准错误输出) 的内容打印出来。
        这样我们就能立刻知道Allure命令为什么执行失败了。
        """
        print("Allure报告生成失败！")
        print("错误信息:", result.stderr)


if __name__ == "__main__":
    # --- 使用 argparse 解析命令行参数 ---
    """
    创建一个参数解析器对象 parser。
    description 是在使用 -h 或 --help 查看帮助信息时显示的脚本描述。
    """
    parser = argparse.ArgumentParser(description="Velotric App自动化测试运行器")

    """
    调用 parser.add_argument() 方法，为我们的脚本定义可以接收哪些命令行参数。
    '-k', '--keyword': 定义一个参数，可以缩写为 -k，也可以全写为 --keyword。
    type=str: 指定这个参数接收的值应该是字符串类型。
    default='.': 为 --path 参数设置一个默认值。如果运行时不提供 --path，它的值就是 . (当前目录)。
    help='...': 定义这个参数的帮助说明文字。
    """
    # 添加 -k 参数，用于按关键字/名称运行测试 (例如: -k test_login)
    parser.add_argument('-k', '--keyword', type=str, help='按关键字运行匹配的测试用例。')

    # 添加 -m 参数，用于按标记运行测试 (例如: -m smoke)
    parser.add_argument('-m', '--marker', type=str, help='运行带有特定标记的测试用例。')

    # 添加 --path 参数，用于指定要运行的测试文件或目录
    parser.add_argument('--path', nargs='+', default=['test_case/'], type=str,
                        help='指定要运行的测试文件或目录，默认为当前目录。')

    """
    调用 parser.parse_args()，它会去检查真正的命令行输入，并把解析到的值存入一个类似字典的对象 args 中。
    比如你运行 python cli.py -k login，那么 args.keyword 的值就是 'login'。
    """
    args = parser.parse_args()

    # --- 组装 pytest 参数 ---
    """
    创建一个空列表 extra_pytest_args，用来存放从命令行接收到的、需要传递给Pytest的参数。
    """
    extra_pytest_args = []
    """检查用户是否在命令行提供了 -k 参数。如果有，args.keyword 就不是 None，条件成立。"""
    if args.keyword:
        """
        extend 方法可以将一个列表的所有元素都添加到另一个列表中。
        这里我们把 -k 这个标志和它对应的值（比如 'login'）作为一个整体 ['-k', 'login'] 添加进去。
        """
        extra_pytest_args.extend(['-k', args.keyword])
    if args.marker:
        """对 -m 参数做同样的处理。"""
        extra_pytest_args.extend(['-m', args.marker])

    # 将测试路径作为最后一个参数
    """
    把 --path 对应的列表（例如 ['path1', 'path2']）中的每一个元素都添加到 extra_pytest_args 列表的末尾。
    """
    extra_pytest_args.extend(args.path)

    # 运行测试
    """
    最后，调用我们之前定义的 run_tests 函数，并把我们刚刚从命令行参数精心组装好的 extra_pytest_args 列表传给它，启动整个测试流程。
    """
    run_tests(extra_pytest_args)

"""
使用说明
1.运行所有测试（默认行为）：
python cli.py

2.只运行登录模块的测试：
python cli.py --path test_case/test_login.py

3.只运行包含 "userinfo" 关键字的测试用例：
python cli.py -k userinfo

4.假设你给某些用例加了标记 @pytest.mark.smoke，可以这样运行：
python cli.py -m smoke

python cli.py --path test_case/test_login.py test_case/test_home.py
"""

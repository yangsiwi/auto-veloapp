# Velotric App 自动化测试框架

## 项目概述

这是一个基于 Appium + Pytest + POM 设计模式的移动应用自动化测试框架，专门为 Velotric 电动自行车应用设计。本框架实现了主要功能模块的自动化测试，包括登录、首页和车辆设置等功能。

## 技术栈

- **编程语言**：Python 3.10.11
- **自动化工具**：Appium
- **测试框架**：Pytest
- **设计模式**：Page Object Model (POM)
- **报告工具**：Allure Report
- **数据驱动**：YAML、Excel

## 项目结构

```
.
├── base                    # 基础类库
│   └── keywords.py         # UI 操作关键字封装
├── conftest.py             # Pytest 配置与前置条件
├── data                    # 测试数据
│   ├── home.yaml           # 首页测试数据
│   ├── login.yaml          # 登录测试数据
│   └── velotric.xlsx       # Excel 格式测试数据
├── locator                 # 元素定位器
│   ├── bike_settings_locator.py
│   ├── home_locator.py
│   ├── info_locator.py
│   └── login_locator.py
├── page                    # 页面对象
│   ├── BikeSettingsPage.py # 车辆设置页面
│   ├── HomePage.py         # 首页
│   ├── InfoPage.py         # 信息页面
│   ├── LoginPage.py        # 登录页面
│   └── riding_page.py      # 骑行页面
├── pytest.ini              # Pytest 配置文件
├── test_case               # 测试用例
│   ├── test_home.py        # 首页测试
│   ├── test_login.py       # 登录测试
│   └── zzztest_riding.py   # 骑行测试
└── utils                   # 工具类
    ├── load_yaml.py        # YAML 文件加载
    └── logger.py           # 日志工具
```

## 设计模式

本项目采用 POM (Page Object Model) 设计模式，将页面元素定位和页面操作方法封装在对应的 Page 类中，主要优势：

1. **代码复用**：页面操作方法可在多个测试用例中复用
2. **易维护**：当 UI 变化时，只需修改对应的 Page 类，而不影响测试用例
3. **可读性**：测试代码更加清晰，易于理解
4. **职责分离**：测试数据、页面操作和测试逻辑分离

## 特性

- **数据驱动**：支持 YAML 和 Excel 格式的测试数据
- **自动截图**：测试失败时自动截图并附加到 Allure 报告
- **动态报告**：使用 Allure 生成美观的测试报告

## 环境配置

### 前提条件

- 安装 Python 3.10 或更高版本环境
- 配置 Android SDK 环境
- 配置 JDK 环境
- 安装 Appium

### 安装依赖

```bash
# 创建虚拟环境
python -m virtualenv venv

# 激活虚拟环境
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

## 运行测试

### 启动 Appium 服务器

```bash
appium --address 127.0.0.1 --port 4723
```

### 运行所有测试

```bash
pytest
```

### 运行特定模块测试

```bash
pytest test_case/test_login.py -v
pytest test_case/test_home.py -v
```

### 生成 Allure 报告

```bash
# 运行测试并生成结果
pytest --alluredir=./allure-results

# 生成报告
allure generate allure-results -o allure-report --clean

# 打开报告
allure open allure-report
```

## 测试数据管理

测试数据存储在 `data` 目录下，支持两种格式：

1. **YAML 格式**：适用于结构化数据
   ```yaml
   - case_id: login001
     case_name: 测试用户名为空
     all_params:
       username: ""
       password: "password123"
     expected_result: "Email can't be empty"
   ```

2. **Excel 格式**：适用于非技术人员编辑的数据
   - 通过 `openpyxl` 库读取并解析

## 扩展与定制

### 添加新页面

1. 在 `locator` 目录下创建新的定位器文件
2. 在 `page` 目录下创建新的页面类
3. 在 `test_case` 目录下创建对应的测试用例

### 自定义关键字

通过扩展 `base/keywords.py` 文件添加新的 UI 操作方法。

## 常见问题

1. **设备连接问题**：确保 Android 设备已启用开发者选项和 USB 调试
2. **Appium 服务器错误**：检查 Appium 服务器是否正常运行
3. **元素定位失败**：查看定位策略是否正确，或元素是否存在


## 许可证

[MIT](LICENSE)

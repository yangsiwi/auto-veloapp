import yaml


# 有yaml文件数据 读取 yaml 文件数据
# 安装yaml pip install pyyaml -i 镜像
# with open(r"E:\hcVip\app\app_project_vip\day13\data\login.yaml",'r',encoding="utf-8") as f:
#     data=yaml.safe_load(f)
#     print(data)

# 测试用例中，拿到 yaml 测试数据  封装成方法 别的地方才好使用
def load_yaml(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        return yaml.safe_load(f)


# 规范的写法是在main里面测试一下
if __name__ == '__main__':
    data = load_yaml("../data/home.yaml")
    print(data)

from jinja2 import Environment,FileSystemLoader
import yaml
import sys
import os

# 与上次实验脚本差异部分，这里我们从CMD取Jinja2模板和yaml配置参数。
template_dir, template_file = os.path.split(sys.argv[1])
vars_file = sys.argv[2]

#过程中有异常，可以去除注释，用print()函数 辅助定位。
# print(template_dir)
# print(template_file)
# print(vars_file)

# 通过template_dir, template_file = os.path.split(sys.argv[1])，模板的位置及模板内容。
env = Environment(
    loader = FileSystemLoader(template_dir),
    trim_blocks=True,
    lstrip_blocks=True)
template = env.get_template(template_file)
# print(template)

# vars_file = sys.argv[2]，获取配置参数内容。
with open(vars_file) as f:
    vars_dict = yaml.safe_load(f)

for sw in vars_dict:
    #print(sw)
    swx_conf = sw['name'] + template_file + '.txt'
    swx_conf = sw['name'] + '_' + template_file[0:template_file.find('.')] + '.txt'
    with open(f'.\\results\\{swx_conf}', 'w') as f:
        f.write(template.render(sw))

print('文件生成完毕！')



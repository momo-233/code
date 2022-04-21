from jinja2 import Environment,FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader('D:\professional programs\\vscode\code\自动化\jinja2\替换变量\\templates'))
template = env.get_template('sw_template.jinja2')

with open('D:\professional programs\\vscode\code\自动化\jinja2\替换变量\sw_info.yaml') as f:
    sws = yaml.safe_load(f)

for sw in sws:
    swx_conf = sw['name'] + '.txt'
    with open(f'D:\professional programs\\vscode\code\自动化\jinja2\替换变量\\results\{swx_conf}', 'w') as f:
        f.write(template.render(sw))


print("文件生成完毕！") 
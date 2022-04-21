from jinja2 import Environment,FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('filters_dictsort.jinja2')

with open('data_files\\filters_dictsort.yaml') as f:
    sws = yaml.safe_load(f)

for sw in sws:
    swx_conf = sw['name'] + '.txt'
    with open(f'results\{swx_conf}', 'w') as f:
        f.write(template.render(sw))


print("文件生成完毕！") 
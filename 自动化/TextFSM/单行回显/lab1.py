import sys
import textfsm
from tabulate import tabulate

with open('1.template') as f, open('output_from_cli') as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(result)
    print(tabulate(result, headers=header))

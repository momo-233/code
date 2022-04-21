import re

disp_int = '''
<Layer3Switch-1>display interface
GigabitEthernet0/0/1 current state : UP
Line protocol current state : UP
Description:
Switch Port, PVID :    1, TPID : 8100(Hex), The Maximum Frame Length is 9216
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 4c1f-cc92-675c
Last physical up time   : 2021-10-25 15:22:35 UTC-08:00
Last physical down time : 2021-10-25 15:22:33 UTC-08:00
......'''

search1 = re.search(r'Switch.+TPID.+Length.+',disp_int).group()
#为什么只匹配了一行？因为 . 这个特殊正则符号在匹配到换行符的时候会停止
print(search1)


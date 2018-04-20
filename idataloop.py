'''代码思路 : 
利用浏览器存放的自己的 Cookie 进行模拟登陆 .
登陆后发出请求 :使用 Requests 库 , BeautifulSoup库 解析 + 获取元素
把今日打卡贴的所有回帖人的姓名昵称记录下来 .
'''

#***************************************************************
# 需要手动输入:  
#     URl 就是当日帖子页的 URL  & 检查元素获取你的登陆 Cookie
url = 'https://bbs.idataloop.com/forum.php?mod=viewthread&tid=1304'

cookie = r'xxxxxxxxxx'

#***************************************************************


import requests
from bs4 import BeautifulSoup

#改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 

# 对 Cookie 进行字典化处理
cookies = {}
for line in cookie.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value

# 编辑 Headers
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

# namelist 存放回帖人的社区昵称.
namelist = list()

# 这里比较粗暴 ,我们就单纯的认为跟帖不会超过十页   ....
i = 1
while True:
    urls = url+'&extra=&page='+str(i)
    while i == 10 : break
    try:
        req = requests.get(urls ,headers = headers, cookies = cookies)
        soup = BeautifulSoup(req.content,'lxml')
        for u in soup.find_all('div',attrs={'class':'authi '}):
            namelist.append(u.find('a',attrs={'target':'_blank'}).text)
        if i>10 : break  
        i+= 1
    except ConnectionError as e:
        break

# 可能有人重复发帖 , 丢 namelist 去重
namelist = list(set(namelist))

print("今天的跟贴人 :")
print(namelist)
input("回车退出")
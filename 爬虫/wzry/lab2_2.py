import requests
import bs4
import re
from lab2_1 import *
import json

def save(items):
    print("save")

url="http://db.18183.com/wzry/"
num=106
#初始化属性

response = requests.get(url)
if response.status_code == 200:
    soup = bs4.BeautifulSoup(response.text,'html.parser')
    #print(soup.prettify())
else:
    print("default")
#获取主页hml

pattern='/wzry/hero/(.*?).html"'
parse_over = re.findall(pattern,response.text, re.S)
for item in parse_over[0:106]:
    url="http://db.18183.com/wzry/hero/"+str(item)+".html"
    avater=get_detail(url)
    file=open('result.json','a',encoding='utf8')
    
    file.write(json.dumps(avater,ensure_ascii=False))
    file.write('\n')
    file.close()
print("success!")
    
#匹配各个角色URL


#if __name__=='__main__':
#    #写上表头
#    print("main")

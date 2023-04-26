import requests
import bs4
import re
result = {
    '英雄名字':'',
    '生存能力':'',
    '攻击伤害':'',
    '技能效果':'',
    '上手难度':''
    }
#print(type(result))

def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.text,'html.parser')
            #print(soup.prettify())
            return soup
        print("default")
    except RequestException:
        print("error")
        return None
#查找URL返回soup
        
def get_parse(soup):
    name = soup.find('h1').text 
    #result["英雄名字"]=name
    #print(name)

    pattern1='class="star star-(.*?)"'
    star = re.findall(pattern1,soup.prettify(), re.S)
    #print(star)

    a=name.split()+star

    c = dict(zip(result.keys(),a))
    print(c)

    buff=str(soup.select('div.hero-panel-update-cont'))
    pattern2='<dt>(.*?)</dt>'
    attr = re.findall(pattern2, buff, re.S)
    for item in attr:
        t=item.split('：' )
        c[t[0]]=t[1]
    del soup
    return c


def get_detail(url):
    soup=get_page(url)
    while soup is None:
        soup=get_page(url)
        
    return get_parse(soup)

    

if __name__=='__main__':
    url="http://db.18183.com/wzry/hero/16364.html"
    print( get_detail(url))
    #soup=get_page(url)
    #get_parse(soup)

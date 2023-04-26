# Python学习——爬虫

![image-20230401104212775](F:\fsl\Python学习-爬虫.assets\image-20230401104212775.png)

## 步骤：

### 数据采集+数据处理——

### 1.发request请求

如果状态200则将text转为soup对象

### 2.三个框框分别进行检索

css匹配：

1.姓名

name = soup.find('h1').text 

正则匹配：

2.星数量

pattern1='class="star star-(.*?)"'

![image-20230407002514108](F:\fsl\Python学习-爬虫.assets\image-20230407002514108.png)

3.属性

buff=str(soup.select('div.hero-panel-update-cont'))
    pattern2='<dt>(.*?)</dt>'
    attr = re.findall(pattern2, buff, re.S)
    for item in attr:
        t=item.split('：' )

![image-20230407002547405](F:\fsl\Python学习-爬虫.assets\image-20230407002547405.png)

#### 2.1 问题1 soup对象None会返回soup没有find函数

​	solution

~~~python
soup=get_page(url)
    while soup is None:
        soup=get_page(url)
~~~

#### 2.2问题2 如何转为dict对象

solution

~~~python
1.c = dict(zip(result.keys(),a))
2.for item in attr:
        t=item.split('：' )
        c[t[0]]=t[1]
~~~

### 3.写get_detail接收url返回dict

### 4.制定遍历策略（lab2_2）

发现英雄的网址后缀不是顺序的

solution——正则表达式匹配

~~~python
pattern='/wzry/hero/(.*?).html"'
parse_over = re.findall(pattern,response.text, re.S)
for item in parse_over[0:106]:
    url="http://db.18183.com/wzry/hero/"+str(item)+".html"
~~~

### 5.遍历调用get_detail转json写入文件



## 参考链接：

[爬虫，从爬取豆瓣开始 ](https://zhuanlan.zhihu.com/p/66661862)

[beautifulsoup css选择器](https://blog.csdn.net/xuebiaojun/article/details/119652358#:~:text=爬虫利器BeautifulSoup之CSS选择器的基本使用 1 1.Beautiful Soup简介 Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。 它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。 Beautiful,你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。 然后，你仅仅需要说明一下原始编码方式就可以了。 ... 2 2. BeautifulSoup 中CSS选择器的基本使用)

[面向零基础小白的爬虫系列（三）：字典_字典 爬虫](https://blog.csdn.net/qq_44921056/article/details/114982647)

[python字典转化为json格式并写入](https://blog.csdn.net/qq_45665594/article/details/116431542)

[python爬取并生成csv文件](https://blog.csdn.net/guihua55/article/details/109347964)
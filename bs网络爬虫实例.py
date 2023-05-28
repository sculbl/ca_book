#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: LBL
@contact:scu_lbl@sina.com
@version: 1.0.0
@license: Apache Licence
@file: bs网络爬虫实例.py
@time: 2023/5/22 18:37
"""
import requests
from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
<title>测试中文网页 - Test Page</title>
</head>
<body>
<div class="content">
<p>This is a paragraph.</p>
<p>这是一个段落。</p>
<a href="http://www.test.com" class="link">Link text</a>
</div>
</body>
</html>
"""


def traverse_tree():
    """
    遍历树
    :return:
    """
    soup = BeautifulSoup(html_doc, 'html.parser')  # BeautifulSoup对象

    # 遍历HTML树
    div = soup.div
    for element in div.descendants:  # 解析BeautifulSoup对象中div所有子节点
        if element.name:
            print(element.name)      # 输出结果(对应元素名)：p  p  a


def parse_html():
    """
    解析网页
    :return:
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.prettify())  # 输出解析后的HTML文档


def find_html_ele():
    """
    搜索html元素
    :return:
    """
    soup = BeautifulSoup(html_doc, 'html.parser')

    # 搜索单个元素
    title = soup.title
    print(title.string)  # 获取title元素的文本值

    # 搜索单个元素（CSS选择器）
    link = soup.select_one('a.link')
    print(link['href'])  # 获取a元素的href属性值

    # 搜索多个元素
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        print(p.string)  # 获取所有p元素的文本值

    # 测试中文网页 - Test Page
    # http://www.test.com
    # This is a paragraph.
    # 这是一个段落。

def crawler_html():
    """
    抓取网页内容
    :return:
    """
    url = "https://www.baidu.com"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    # 获取标题
    title = soup.title.string
    print("网页标题：", title)

    # 获取所有链接
    links = soup.find_all('a')
    print("所有链接地址：")
    for link in links:
        print(link.get('href'))

    # 网页标题： 百度一下，你就知道
    # 所有链接地址：
    # http://news.baidu.com
    # https://www.hao123.com
    # ...


def parse_xml():
    """
    解析xml文档
    :return:
    """
    xml_doc = """
    <root>
        <person id="1001">
            <username>张三</username>
            <age>25</age>
            <email>zhangsan@example.com</email>
        </person>
        <person id="1002">
            <username>李四</username>
            <age>30</age>
            <email>lisi@example.com</email>
        </person>
    </root>
    """
    soup = BeautifulSoup(xml_doc, 'xml')

    # 搜索单个元素
    person = soup.find('person', {'id': '1001'})
    print(person.username.string)  # 输出：张三

    # 搜索单个元素（CSS选择器）
    email = soup.select_one('person[id="1002"] email')
    print(email.string)  # 输出：lisi@example.com

    # 搜索多个元素
    persons = soup.find_all('person')
    for p in persons:
        print(p['id'], p.username.text, p.email.text)

    # 输出：
    # 1001 张三 zhangsan@example.com
    # 1002 李四 lisi@example.com


def main():
    # parse_html()
    # find_html_ele()
    # traverse_tree()
    # crawler_html()
    parse_xml()


if __name__ == '__main__':
    main()

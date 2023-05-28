#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: LBL
@contact:scu_lbl@sina.com
@version: 1.0.0
@license: Apache Licence
@file: 简单的网络爬虫程序.py
@time: 2023/5/22 16:18
"""
import requests
from bs4 import BeautifulSoup


def main():
    # 请求URL并抓取数据
    url = 'https://www.baidu.com'
    response = requests.get(url)
    html_str = response.text.encode("utf-8")

    # 使用BeautifulSoup解析HTML数据
    soup = BeautifulSoup(html_str, "html.parser")
    title = soup.find('title').get_text()  # 获取网页标题
    links = [link.get('href') for link in soup.find_all('a')]  # 获取所有链接地址

    # 打印结果
    print('网页标题：' + title)
    print('所有链接地址：')
    for link in links:
        print(link)


def solve_code():
    """
    设置HTTP请求头时添加了“Accept-Encoding”字段，以便网站以正确的编码方式响应
    并通过.encode("utf-8")对Unicode编码进行了转换
    :return:
    """
    url = 'https://www.baidu.com'
    headers = {'Accept-Encoding': 'gzip, deflate, br'}  # 设置请求头
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding  # 检查编码方式并转换为UTF-8
    html_str = response.text.encode("utf-8")

    soup = BeautifulSoup(html_str, "html.parser")
    title = soup.find('title').get_text()
    links = [link.get('href') for link in soup.find_all('a')]

    print('网页标题：' + title)
    print('所有链接地址：')
    for link in links:
        print(link)


def test_get():
    """
    测试get请求
    :return:
    """
    url = "https://www.baidu.com"  # 链接地址
    response = requests.get(url)  # 请求响应

    print("HTTP 响应状态码:", response.status_code)
    print("HTTP 响应体:", response.text)


def test_post():
    """
    测试post请求
    :return:
    """
    url = "https://httpbin.org/post"
    data = {"username": "testuser", "password": "testpass"}
    response = requests.post(url, data=data)

    print(response.status_code)
    print(response.json())


def test_http():
    """
    测试http headers
    :return:
    """
    import requests

    url = "https://www.baidu.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)

    print(response.status_code)
    print(response.text)


def test_upload_file():
    """
    测试上传文件
    :return:
    """
    url = "https://httpbin.org/post"
    files = {'file': open('example.txt', 'rb')}  # 注意先新建example.txt
    response = requests.post(url, files=files)

    print(response.status_code)
    print(response.json())


def test_poxies():
    """
    测试代理
    :return:
    """
    url = "https://httpbin.org/get"
    proxies = {
        'http': 'http://xxxx.xx.x.xxxx:xxxx',
    }
    response = requests.get(url, proxies=proxies)

    print(response.status_code)
    print(response.json())


def test_session():
    """
    测试cookies
    :return:
    """
    url = "https://httpbin.org/cookies"
    session = requests.Session()
    response = session.post(url, data={'message': 'test message'})

    print(response.status_code)
    print(response.json())


if __name__ == '__main__':
    test_session()
    # test_poxies()
    # test_upload_file()
    # test_http()
    # test_post()
    # test_get()
    # main()
    # solve_code()

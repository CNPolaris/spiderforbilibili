# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 11:09
# @FileName: spider_bilibili.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris


import random
import requests
import jieba
import numpy as np
from lxml import etree


class SpiderBiliBili():
    def __init__(self):
        # 用来伪装成浏览器的头部 防止触发网站的反爬虫机制
        self.user_agent = ["Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
                           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; 360SE) ",
                           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0) ",
                           "Mozilla/5.0 (Windows NT 5.1; zh-CN; rv:1.9.1.3) Gecko/20100101 Firefox/8.0",
                           "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
                           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
                           "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
                           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; TencentTraveler 4.0; .NET CLR 2.0.50727)",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
                           ]

        # 目标地址
        # 格式 https://api.bilibili.com/x/v1/dm/list.so?oid=目标视频的oid号
        self.url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=184632909'
        self.html = None

    def spider_main(self):
        # 随机生成头部,避免同样的头部访问过多触发反爬虫
        headers = {
            "User-Agent": random.choice(self.user_agent)
        }
        spider = requests.get(self.url, headers=headers)

        self.html = etree.HTML(spider.content)
        danmu_list = self.html.xpath('//i//d//text()')
        print(danmu_list)
        with open('danmu.txt', 'a', encoding='utf-8')as f:
            for t in danmu_list:
                f.write(t + '\n')


if __name__ == '__main__':
    bilibili = SpiderBiliBili()
    bilibili.spider_main()

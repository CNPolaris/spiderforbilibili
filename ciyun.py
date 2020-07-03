# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 14:26
# @FileName: ciyun.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris


import jieba
from wordcloud import WordCloud

# 数据集文件位置
filename = "E://GitHub//spiderforbilibili//danmu.txt"
# 生成词云图片的保存位置和格式
savePicture = "词云.png"
# 字体格式
fontpath = "simhei.ttf"
# 1.读入数据集
file_text = open(filename,'r', encoding="utf-8").read()
# 2.设置词云的背景颜色、字体、字号
cloud = WordCloud(
    # 字体格式
    font_path=fontpath,
    # 背景色
    background_color="black",
    # 允许最大词汇
    max_words=2000,
    # 最大号字体
    max_font_size=60
)
# 3.jieba分词
secondhome_words1 = jieba.cut(file_text)
last_text = " ".join(secondhome_words1)
# 4.开始生成词云
word_cloud = cloud.generate(last_text)
# 5.保存词云
word_cloud.to_file(savePicture)


# spiderforbilibili
在刷B站的时候突发奇想，想着用python试着爬取B站视频弹幕，看看广大网友们的才华[doge]。

# 准备工作

在开始之前，按照惯例先研究一下B站的网页的代码找到需要的弹幕链接。刚开始找的时候有点麻烦，然后参照了一下网上的资料后，发现B站视频的特点是可以根据视频主键标识的**oid**就可以得到弹幕，下面是一般使用地址。

[https://api.bilibili.com/x/v1/dm/list.so?oid=目标视频的oid](https://api.bilibili.com/x/v1/dm/list.so?oid=)

至于**oid**怎么查看呢？

找到oid可以在网页上通过F12查看网页信息，刷新后就可以找到**oid**

![](%E6%9F%A5%E6%89%BEoid.png)

# 开始工作

1.弹幕爬虫

[]()
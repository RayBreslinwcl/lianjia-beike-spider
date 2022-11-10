#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 二手房信息的数据结构


class ErShou_Each(object):
    def __init__(self, district, area, name, price, desc, pic ,interest =0,publicday=0,xiaoqu='无名'):
        self.district = district
        self.area = area
        self.price = price
        self.name = name
        self.desc = desc
        self.pic = pic
        # 添加更加热点信息
        #（1）关注人数：21人关注
        self.interest = interest
        #（2）发布天数：25天以前发布
        self.pubicday =publicday
        #（3）小区名称：瑞和苑 - 周浦
        self.xiaoqu =xiaoqu


    def text(self):
        return self.district + "," + \
                self.area + "," + \
                self.name + "," + \
                self.price + "," + \
                self.desc + "," + \
                self.pic + "," + \
                self.interest + "," + \
                self.pubicday + "," + \
                self.xiaoqu

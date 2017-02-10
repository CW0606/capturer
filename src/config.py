# coding:utf-8
import time
import os

# 当前文件路径
current_dir_path = os.getcwd()

# 获取公式区间正则匹配表达式
re_express = [u""]

# html 暂存路径
html_save_tmp_path = os.path.join(current_dir_path, 'html_tmp')

# png 存储路径
png_path = os.path.join(current_dir_path, 'pngs')

#screenshot 临时存储路径
screenshot_path = os.path.join(current_dir_path, 'screenshot')


# png 命名规则
def get_png_name():
    return long(time.time())


# mysql 配置信息
mysql_config = {}

# mongodb 配置信息
mongodb_config = {}

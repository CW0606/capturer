# coding:utf-8
"""
    截图实现:
            1. 使用正则表达式获得文本中的所有包含公式的相关html源码
            2 将1中获得的源码进行格式构建成可截图html代码
            3 将2中构建好的html代码存储到临时html文件存储位置
            4 使用selenium调用浏览器打开3中生成的html文件，对其进行截图
    图片替换:
            1.将正则匹配的公式文本替换成公式文本对应图片地址的img标签

    注意:代码中使用的所有输入必须使用unicode编码
"""
import config
import re
import codecs
import time
import os
from selenium import webdriver
from PIL import Image


class Capture(object):
    """

    """

    def __init__(self):
        self.driver = webdriver.Chrome()
        pass

    def get_math_express(self, src_html):
        """
        使用正则表达式获取src_html 中符合转成图片的相关源码
        :param src_html:
        :return:
        """
        if src_html is None or len(src_html) == 0:
            return {src_html: None}
        math_express_list = list()
        # todo  获得所有满足的公式文本 添加到 math_express_list
        return {src_html: math_express_list}

    def generate_valid_html(self, math_express, css_path=None):
        """将匹配成功的代码添加标签"""
        if css_path is None:
            css_path = u'style.css'
        return u"""<html> <link rel="stylesheet" type="text/css" href="{
        css_path}"><head></head><body><font size="5">{
        math_express}</font></body></html>""".format(
            math_express=math_express, css_path=css_path)

    def save_valid_html(self, valid_html):
        filename = str(time.time() * 10000) + '.html'
        file_path = os.path.join(config.html_save_tmp_path, filename)
        with codecs.open(filename=file_path, mode='wb', encoding='utf-8') as f:
            f.write(valid_html)
        return file_path

    def draw(self, html_path):
        """根据html_path 获取html 中公式的截图"""
        url = "file://" + html_path
        self.driver.get(url)
        element = self.driver.find_element_by_tag_name('font')
        screenshot_name = str(time.time() * 10000) + '.png'
        screenshot_path = os.path.join(config.screenshot_path, screenshot_name)
        self.driver.save_screenshot(screenshot_path)
        return self._crop(element=element, screenshot_path=screenshot_path)

    def _crop(self, element, screenshot_path):
        """截图"""
        img = Image.open(screenshot_path)
        left = int(element.location['x'])
        top = int(element.location['y'])
        right = left + element.size['width']
        bottom = top + element.size['height']
        window = (left, top, right, bottom)
        region = img.crop(window)
        png_name = str(time.time() * 10000) + '.png'
        png_path = os.path.join(config.png_path, png_name)
        region.save(png_path)
        return png_name

    def _replace(self, html_content, math_express, png_name):
        if html_content is None:
            raise Exception("html content 不能为空")
        if math_express is None or png_name is None:
            return html_content
        img_png_name = u"""<img src="{png_name}">""".format(png_name=png_name)
        return html_content.replace(math_express, img_png_name)

    def capture(self, html_content=None, html_path=None):
        """解析从数据库里面输入的html文本"""
        if html_content is None:
            if html_path is None:
                raise Exception('不能全为空')
            html_content = u""
            with codecs.open(html_path, mode='rb', encoding="utf-8") as f:
                html_content += f.read()
        # 获得html_content 和 所有满足的公式文本
        re_data = self.get_math_express(html_content)
        replace_html_content = html_content
        math_express_list = re_data[html_content]
        if math_express_list is None or len(math_express_list) == 0:
            return replace_html_content
        for math_express in re_data[html_content]:
            valid_html = self.generate_valid_html(math_express)
            valid_html_path = self.save_valid_html(valid_html)
            png_name = self.draw(valid_html_path)
            replace_html_content = self._replace(replace_html_content,
                                                 math_express, png_name)
        return replace_html_content

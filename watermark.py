# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:38:08 2021
"""
 

import os
from PIL import ImageFont, ImageDraw, Image
 
path_name = os.path.abspath('.')
 
 
def add_watermark(img_path='', text='', degree='45', font_path='Deng.ttf'):
    '''
    图片加文字水印，不兼容python3，需要安装Pillow：pip install Pillow==5.0.0
    :param base64_img: 图片的base64编码，如果想直接处理图片只需要base64_img='图片的路径'，并将下面第一行代码改为：
                       Image.open(base64_img).convert('RGBA')
    :param font_path: 水印的字体路径
    :param text: 水印的文字内容，windows下要u''不能'', 否则乱码
    :return: None
    '''
    # 图片加载到内存流，RGBA模式(可以设置透明度)，不用保存base64还原的图片
    # with Image.open(base64_img).convert('RGBA') as img:
    with Image.open(img_path).convert('RGBA') as img:
        # 新建图层，RGBA模式
        size = max(img.size)
        s2 = max(img.size) // 7
        new_img = Image.new(
            'RGBA',
            # 比图片大，后面要调角度并裁剪（大小需要自己根据后面的角度调，如果只需要水平的水印，大小和图片相同即可，后面也不用rotate和crop）
            (size * 2, size * 2),
            # 新图层的RGB值以及透明度(透明度为0表示完全透明)
            (0, 0, 0, 0)
        )
        # 设置字体及大小，参数为字体的路径，要支持中文，否则中文不显示或乱码
        font = ImageFont.truetype(font_path, size=s2//5)
        # 在新图层上画文字水印
        for j in range(size//s2*2):
            for i in range(size//s2):
                ImageDraw.Draw(new_img).text(
                    # 文字的坐标，j%2是为了让相邻两行水印错开
                    (new_img.size[0] - s2 * (j % 2) - s2*2 * i, new_img.size[1] - s2 * j),
                    # 水印的文字内容
                    text=text,
                    # 字体
                    font=font,
                    # 文字的颜色，分别对应RGB值和透明度
                    fill=(130, 130, 130, 130)
                )
        #new_img.show()
        # 将新图层旋转30度后裁剪和图片一样大，新图层必须和图片一样大，否则无法合并
        x = int(img.size[0] * 0.5)
        y = int(img.size[1] * 0.5)
        x1 = x + img.size[0]
        y1 = y + img.size[1]
        new_img = new_img.rotate(degree).crop((x,y,x1,y1))
        print(img.size,new_img.size)
        #new_img.show()
        # 合并图层
        img_watermark = Image.alpha_composite(img, new_img)
    # 打开新图片
    img_watermark.show()
    # 保存到指定路径
    img_watermark.save(img_path + '_wk.png', 'png')
    return None
 
 
if __name__ == '__main__':
    try:
        base64_img = '1.jpg'
        base64_img = '1.jpg'
        base64_img = '1.jpg'
        # 字体路径
        font_path = ''
        text = '仅限残疾保险使用'
        add_watermark(base64_img, text,-45)
    except Exception as e:
        print('哪里出错了: %s' % e)
        raise

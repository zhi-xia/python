import os
import re
import time
import urllib
import urllib.request
from socket import socket


def delRepeat(a):
    for x in a:
        while a.count(x) > 1:
            del a[a.index(x)]
    return a


def name(photo):
    a = photo[33:]
    b = a.replace("%20", "_").replace("%28", "(").replace("%29", ")")
    return b


def save_img(img_url, file_name, file_path='C:\\Users\\86137\\Pictures\\Saved Pictures\\爬虫图片'):
    # 保存图片到磁盘文件夹 file_path中
    try:
        if not os.path.exists(file_path):
            print('文件夹', file_path, '不存在，重新建立')
            os.makedirs(file_path)
        file_suffix = os.path.splitext(img_url)[1]  # 获得图片后缀
        filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)  # 拼接图片名（包含路径）
        urllib.request.urlretrieve(img_url, filename=filename)  # 下载图片，并保存到文件夹中
    except IOError as e:
        print('文件操作失败', e)
    except Exception as e:
        print('错误 ：', e)


for page in range(1, 10):  # 填入爬取1-10页
    time.sleep(3)
    url = "https://yande.re/post?page=" + str(page) + "&tags=machikado_mazoku"  # 这个tag自己填写
    html = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    find_index = re.findall(r'id="p\d{3,}', html)
    count = 0
    for each in find_index:  # 搜索每一张图
        try:
            time_start = time.time()
            count += 1
            words = "正在保存第" + str(page) + "页，第" + str(count) + "张图"
            print(words, end='')
            n = each[5:]
            page_url = "https://yande.re/post/show/" + str(n)
            page_html = urllib.request.urlopen(page_url).read().decode("utf-8", "ignore")
            photo_find = delRepeat(re.findall(r'href="https://files.yande.re/image/([\s\S]*?)"', page_html))
            if len(photo_find) == 0:
                continue
            photo_url = "https://files.yande.re/image/" + photo_find[0]
            photo_name = name(photo_find[0])
            save_img(photo_url, photo_name)
            time_end = time.time()
            print(' 用时%d秒 ' % (time_end - time_start))
        except urllib.error.URLError or socket.gaierror or NameError or ConnectionAbortedError as e:
            print('错误 ：', e)
            continue

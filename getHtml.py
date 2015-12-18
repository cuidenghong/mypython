#coding=utf-8
import urllib
import re
import time
from MySQL import MySQL

#执行方法
def init(url):
	return getHtml(url)

#获取页面数据
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return getImg(html)

#获取图片
def getImg(html):
    #reg = r'src="(.+?\.jpg)"'
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    #print imglist
    #return 
    return readImg(imglist)

def readImg(imglist):
    if imglist:
        x = 0 
        for imgUrl in imglist:
            fileName = 'dodoca/dodoca_'
            fileName = fileName + str(x)

            urllib.urlretrieve(imgUrl,'%s.jpg' % fileName,schedule)
            #写入数据库
            insert(imgUrl,fileName)
            x+=1
            #print imgUrl
    return 1		


def schedule(a, b, c):  
    #回调函数
    #@a: 已经下载的数据块
    #@b: 数据块的大小
    #@c: 远程文件的大小
    #''' 
    per = 100.0 * a * b / c 
    if per > 100: 
        per = 100 
    print '%.2f%%' % per

def insert(imgUrl,fileName):
    db = MySQL()
    sql = " insert into w_pic (filename,imgurl,create_time) values ('%s','%s','%s')" % (fileName + '.jpg',imgUrl,time.time())
    print sql
    result = db.insert(sql);
    print result



url = "http://tieba.baidu.com/p/2460150866"
url = "http://www.sina.com.cn"
html = init(url)



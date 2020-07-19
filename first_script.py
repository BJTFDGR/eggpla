import sys
import requests
import urllib.parse
import logging
import time
import pyquery
import random
import functools
import re
import io
import urllib.request
import http.cookiejar
import socket
import urllib.request
from contextlib import closing
from subprocess import call
import os
import pandas as pd
from os import path
from selenium import webdriver
import time
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from multiprocessing import Pool
import multiprocessing
from multiprocessing import Pool
import sys
import requests
import urllib.parse
import logging
import time
import random
import functools
import re
import io
import urllib.request
import http.cookiejar
import socket
import urllib.request
from contextlib import closing
from subprocess import call
import os
import webbrowser as web
from os import path
from selenium import webdriver
import time
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from multiprocessing import Pool
import multiprocessing
from datetime import datetime
import csv
import multiprocessing
import time
#从91avv转到onecut

def getcontent(name):
    #scrape a website return content
    data = {'contents': name}
    post_data = urllib.parse.urlencode(data).encode('utf-8')
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
    }
    # 登录时表单提交到的地址（用开发者工具可以看到）
    req = urllib.request.Request(name, headers=headers,data=post_data)
    cookie = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    content = opener.open(req).read().decode('utf-8')

    return content

def analysispagecontent(content):
    #analysis the page content and write in
    pattern = re.compile('href="/video/view/(.*)</a>')
    file24 = re.findall(pattern,content)
    cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]") # 匹配不是中文、大小写、数字的其他字符

    with open("nameweb.csv","a",encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        for webandname in file24:
            name=webandname.split('">')[1]
            name = cop.sub('', name)
            website='http://91porny.com/video/view/'+webandname.split('">')[0]

            flag=0
            for item in ['熟','肛','同性','干妈','足交','大妈','站街','阿姨']:
                if name.find(item)!=-1:
                    flag=1
                    continue

            if flag==1:
                continue
            writer.writerow([name,website])
            print('name: '+name)         
            print('web: '+website)           

#利用panda去重复
def deleterepilca(csvfile):

    df = pd.read_csv(csvfile,header=0)
    datalist = df.drop_duplicates()
#    datalist=df.drop(df.columns[[0, 1]], axis=1)
    datalist.to_csv(csvfile,index=False)


def download_item(res):
    if res is None:
        print("NONE")
        return
    truewebsite=res[0]
    authorname=res[1]
    titlename=res[2]

    flag=0
    for item in ['熟','肛','同性','干妈','足交','大妈','站街','阿姨','坦']:
        if item in titlename:
            flag=1
    if flag:
        print('PASS IT')
        return

    OutPutFileName = authorname+' '+titlename + '.mp4'

    if os.path.exists('F:\Vedio\\'+OutPutFileName):
        print('REPLICA #  ' + OutPutFileName)
        return
       
    IDM = r'F:\IDM\Internet Download Manager\IDMan.exe'

    DownUrl = truewebsite.replace("http://138.128.27.218//", "http://198.255.82.91//")

    DownPath = r'F:/Vedio'
    call([IDM, '/d', DownUrl, '/p', DownPath, '/f', OutPutFileName, '/n', '/a'])
    print('DOWNLOAD: ')
    print(truewebsite,authorname,titlename)


def singlepageanalysis(website):
    try:
        content=getcontent(website)
    except:
        return
    
    pattern_1 = re.compile('<source src="http(.*)"')
    res3 = re.findall(pattern_1,content)
    truewebsite='http'+res3[0].split('"')[0]


    pattern_1 = re.compile('<meta name="(.*)"')
    res3 = re.findall(pattern_1,content)
    cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]") # 匹配不是中文、大小写、数字的其他字符
    for item in res3:
        if 'twitter:creator' in item:
            authorname=item.split('"')[2]
            authorname = cop.sub('', authorname)
            continue
    for item in res3:
        if 'twitter:title' in item:
            titlename=item.split('"')[2]
            continue        

      
    if [truewebsite,authorname,titlename] is None:
        print("NONE")
        return


    download_item([truewebsite,authorname,titlename])
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    return [truewebsite,authorname,titlename]

def printProgress(iteration, total, prefix='', suffix='', decimals=1, barLength=100):
    """
    Call in a loop to create a terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    
    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '#' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


if __name__=='__main__':
    

    webhead='https://91porny.com/video/category/all/'
    startflag=input()
    if startflag!='0':
        for i in range(1,1001): 
            print('#######################    '+str(i)+'    #########################')
            content=getcontent(webhead+str(i))
            analysispagecontent(content)
    
    #default use all of the columns
    deleterepilca('nameweb.csv')
    

    lasttimeflag=21334
    number=0
    
    
#multi process https://blog.csdn.net/jinping_shi/article/details/52433867
    p = Pool(4)   # 创建4个进程
    with open('nameweb.csv', 'r',encoding="utf-8") as inf:
        reader = csv.reader(inf)
        #totalnum=len(list(reader)) #make reader a list /WRONG
        for line in reader:
            number=number+1
            #printProgress(number,totalnum)

            if lasttimeflag>0:
                lasttimeflag=lasttimeflag-1
                continue

            filename=line[0]
            website=line[1]    
    
            p.apply_async(singlepageanalysis, args=(website,))

    p.close()
    p.join()
    print()

'''no use pool
    with open('nameweb.csv', 'r',encoding="utf-8") as inf:
        reader = csv.reader(inf)
        for line in reader:
            filename=line[0]
            website=line[1]
            
            res=singlepageanalysis(website)  
            if res is None:
                print("NONE")
                continue
            else:
                [truewebsite,authorname,titlename]=res           
            download_item([truewebsite,authorname,titlename])
            
'''            
        




    

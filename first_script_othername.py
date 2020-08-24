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
import sys
import requests
import logging
import random
import functools
import os
import webbrowser as web
from os import path
from selenium.webdriver.common.by import By
import datetime
import time
from multiprocessing import Pool
import multiprocessing
from datetime import datetime
import csv
import pandas as pd

'''
combine files of 91avv
download videos from the same author (amount at limit 100)
try to split words and use a more simple method to detect headline
'''


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
            for item in ['熟','同性','干妈','大妈','站街','阿姨']:
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
    for item in ['熟','同性','干妈','大妈','站街','阿姨']:
        if item in titlename:
            flag=1
    if flag:
        print('PASS IT')
        return

    OutPutFileName = authorname+' '+titlename + '.mp4'

    if os.path.exists('F:\Vedio\\'+OutPutFileName):
        print('')
        return

    if os.path.exists('G:\91down\\'+OutPutFileName):
        print('')
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

def get_file_list(file_path):
    #seq follows time
    dir_list = os.listdir(file_path)
    if not dir_list:
        return
    else:
        # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
        # os.path.getmtime() 函数是获取文件最后修改时间
        # os.path.getctime() 函数是获取文件最后创建时间
        dir_list = sorted(dir_list,  key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
        # print(dir_list)
        return dir_list

def file_split(filePath):
    #split file_name in original file pocket(no input)
    #return filelist in a Two dimension list [[name,filename]]
    totalfilelist=get_file_list(filePath)

    for item in reversed(totalfilelist):
        if ' ' in item:
            authorname.append(item.split(' ')[0])
            filename.append(item.split(' ')[1])
            combine_file.append(item.split(' '))

def restartfrom_zero(startflag):
    #recollect all vedios from the website
    if startflag!='0':
        for i in range(1,3001): 
            print('#######################    '+str(i)+'    #########################')
            content=getcontent(webhead+str(i))
            analysispagecontent(content)   

def allothervideo(authorname):
    website=namehead+authorname
    try:
        content=getcontent(website)
    except:
        return
    pattern_1 = re.compile('<source src="http(.*)"')
    res3 = re.findall(pattern_1,content)
    truewebsite='http'+res3[0].split('"')[0]



if __name__=='__main__':
    
    webhead='https://91porny.com/video/category/all/'
    namehead='https://91porny.com/author/'
    vedio_filePath = 'F:/Vedio'
    lasttimeflag=21334
    number=0
    #list show as glodal num can be transfered instantly
    authorname=[]
    filename=[]
    combine_file=[[]]
    
    startflag=input() or '0'
    restartfrom_zero(startflag)
    
    deleterepilca('nameweb.csv')
    file_split(vedio_filePath)

    #check all other video
    p = Pool(1)   # 创建4个进程
    for name in authorname:     
        p.apply_async(allothervideo, args=(name,))

    p.close()
    p.join()
    print()  
 
    #multi process https://blog.csdn.net/jinping_shi/article/details/52433867
    p = Pool(4)   # 创建4个进程
    with open('nameweb.csv', 'r',encoding="utf-8") as inf:
        reader = csv.reader(inf)
        reader=list(reader)
        reader=list(reversed(reader))  
        #totalnum=len(list(reader)) #make reader a list /WRONG
        for line in reader:
            number=number+1
            #printProgress(number,totalnum)

            filename=line[0]
            website=line[1]      
            p.apply_async(singlepageanalysis, args=(website,))

    p.close()
    p.join()
    print()      
        




    

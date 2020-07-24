import os
import sys
import xlwt
from moviepy.editor import VideoFileClip
 
file_dir = u"G:/视频目录/" #定义文件目录
 
class FileCheck():
 
    def __init__(self):
        self.file_dir = file_dir
    
    def get_filesize(self,filename):
        u"""
        获取文件大小（M: 兆）
        """
        file_byte = os.path.getsize(filename)
        return self.sizeConvert(file_byte)
 
    def get_file_times(self,filename):
        u"""
        获取视频时长（s:秒）
        """
        clip = VideoFileClip(filename)
        file_time = self.timeConvert(clip.duration)
        return file_time
 
    def sizeConvert(self,size):# 单位换算
        K, M, G = 1024, 1024**2, 1024**3
        if size >= G:
            return str(size/G)+'G Bytes'
        elif size >= M:
            return str(size/M)+'M Bytes'
        elif size >= K:
            return str(size/K)+'K Bytes'
        else:
            return str(size)+'Bytes'
    
    def timeConvert(self,size):# 单位换算
        M, H = 60, 60**2
        if size < M:
            return str(size)+u'秒'
        if size < H:
            return u'%s分钟%s秒'%(int(size/M),int(size%M))
        else:
            hour = int(size/H)
            mine = int(size%H/M)
            second = int(size%H%M)
            tim_srt = u'%s小时%s分钟%s秒'%(hour,mine,second)
            return tim_srt
 
    def get_all_file(self):
        u"""
        获取视频下所有的文件
        """
        for root, dirs, files in os.walk(file_dir):  
            return files #当前路径下所有非目录子文件


path = "F:/Vedio" #文件夹目录
os.chdir(path)#change dir


def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    return round(fsize, 2)


bignamelist=[]
namedist={}
files= os.listdir(path) #得到文件夹下的所有文件名称
for file_1 in files: #遍历文件夹
    wholename=path+"/"+file_1
    filesize=get_FileSize(wholename)
    if filesize>5:
        name=file_1.split(' ')[0]
        if name not in bignamelist:
            bignamelist.append(name)
            namedist[name]=[[0],[]]


for file_1 in files: #遍历文件夹
    name=file_1.split(' ')[0]
    if name in bignamelist:
        namedist[name][1].append(file_1)
        wholename=path+"/"+file_1
        filesize=get_FileSize(wholename)
        namedist[name][0][0]=namedist[name][0][0]+int(filesize)


namelist=sorted(namedist.items(),key=lambda item:item[1][0][0])
for item in namelist:
    print()
    




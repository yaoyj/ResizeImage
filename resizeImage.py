#!/usr/bin/env python
# coding=utf-8

from PIL import Image
import glob,os
import numpy as np


# 批量处理各个文件夹下的图像
def resize_imgBatch(folder, new_folder):
    folder_path = glob.glob(folder + '/*.jpg')
    print folder_path
    
    for files in folder_path:
        file_path, file_name = os.path.split(files)
        filter_name, exts = os.path.splitext(file_name)
        
        #判断new_folder是否存在
        if (os.path.isdir(new_folder) == False):
            os.makedirs(new_folder) # 递归地创建不存在的文件夹
        img = Image.open(files)
        
        # 判断是否是RGB图像，不是则灰度转为RGB
        im_array = np.array(img)
        
        if im_array.shape != (224,224,3):
            print "===================="
            im_RGB = img.convert('RGB')
            im_return = im_RGB.resize((224,224))  # w,h
            im_return.save(new_folder + '/' + filter_name + '.jpg')
        
        
        
if __name__=='__main__':
    #遍历目录
    father_path = '17flowers/'
    new_father_path = '17flowers_resized'
    folder_list = os.listdir(father_path)
    
    for folder in folder_list:
        children_folder = os.path.join(father_path, folder)
        new_children_folder = os.path.join(new_father_path, folder)
        resize_imgBatch(children_folder, new_children_folder) #调用resize_imgBatch
    print "done!"
    

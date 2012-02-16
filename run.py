#!/usr/bin/env python
#coding=utf-8

'''
@author: stonelee 
@email: istonelee@gmail.com
@blog: http://stonelee.info
@description: build in Ext JS 4

最终生成文件：
1.all-debug.js 未压缩的打包文件,供调试使用
2.all.js 压缩打包文件,生产环境使用
'''

import os
import jsb3
import parse

FILE_NAME = '../app.jsb3'

BEFORE_NAME = '../temp-before.js'
AFTER_NAME = '../temp-after.js'

def main():
    jsb3.create_jsb(FILE_NAME,BEFORE_NAME,AFTER_NAME)
    os.system('sencha build -p %s -d ../' %(FILE_NAME))

def remove_file(filename):
    if os.path.isfile(filename):
        os.remove(filename)

if __name__ == '__main__':
    main()
    remove_file(BEFORE_NAME)
    remove_file(AFTER_NAME)


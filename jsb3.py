#!/usr/bin/env python
#coding=utf-8

'''
@author: stonelee 
@email: istonelee@gmail.com
@blog: http://stonelee.info
@description: create jsb3 file in Ext JS 4

将app下的js文件按照model, store, view, controller的顺序来创建jsb3。
如果view中使用requires加载其它view，则按照依赖顺序先行加载。
'''

import os
import parse
import sort

APP_NAME = 'CIIS'
APP_PATH = '../app/'
APPJS_PATH = '../app.js'
LICENSE_TEXT = 'Copyright(c)'

def js_loop(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            #只解析js
            if os.path.splitext(filename)[1] == '.js':
                yield root,filename

def simple_loop(path):
    for root,filename in js_loop(path):
        i = root.index('app/')
        path = root[i:]
        yield '{"path": "%s/","name": "%s"},' %(path,filename)


def parse_view_name(path,appName):
    '''
    >> parse_view_name('../app/view/coalbusinesslicense/List.js','CIIS')
    'CIIS.view.coalbusinesslicense.List'
    '''
    i = path.index('/view/')
    s = path[i:]
    s = s.replace('/','.')
    s = os.path.splitext(s)[0]
    s = appName+s
    return s

def get_view_names(path):
    views = {}
    for root,filename in js_loop(path):
        filepath = os.path.join(root,filename)
        viewName = parse_view_name(filepath,APP_NAME)

        f = open(filepath)
        data = f.read()

        requires = parse.parse_requires(data)
        if requires:
            views[viewName] = requires
        else:
            views[viewName] = []

        f.close()
    return views

def parse_jsb_view(viewName):
    '''
    >> parse_jsb_view('CIIS.view.coalbusinesslicense.List')
    {"path": "app/view/coalbusinesslicense/","name": "List.js"}
    '''
    names = viewName.split('.')

    i = names.index('view')
    path_list = names[i:-1]
    path_list.insert(0,'app')
    path = '/'.join(path_list)

    name = names[-1] + '.js'
    return '{"path": "%s/","name": "%s"},' %(path,name)

def view_loop(path):
    views = get_view_names(path)
    views = sort.sort_by_require(views)
    for view in views:
        yield parse_jsb_view(view)


def skeleton(files,before,after):
    return '''
    {
        "projectName": "%s",
        "licenseText": "%s",
        "builds": [
            {
                "name": "All Classes",
                "target": "all-debug.js",
                "options": {
                    "debug": true
                },
                "files": [%s,%s%s]
            },
            {
                "name": "Application - Production",
                "target": "all.js",
                "compress": true,
                "files": [
                    {
                        "path": "",
                        "name": "all-debug.js"
                    }
                ]
            }
        ],
        "resources": []
    }
    ''' %(APP_NAME,LICENSE_TEXT,before,files,after)

def get_files():
    model_path = APP_PATH+'model'
    store_path = APP_PATH+'store'
    view_path = APP_PATH+'view'
    controller_path = APP_PATH+'controller'

    files = ''
    for path in [model_path,store_path]:
        for afile in simple_loop(path):
            files += afile

    for afile in view_loop(view_path):
        files += afile

    for afile in simple_loop(controller_path):
        files += afile

    return files

def get_jsb(before_name,after_name):
    def get_file_name(name):
        return name[name.rindex('/')+1:]

    before = '{"path": "","name": "%s"}' %get_file_name(before_name)
    after = '{"path": "","name": "%s"}' %get_file_name(after_name)
    files = get_files()
    return skeleton(files,before,after)

def create_before_after(appjs,before_name,after_name):
    f = open(appjs)
    data = f.read()
    data = parse.close_autoload(data)
    before, after = parse.split_appjs(data)
    f.close()

    f = open(before_name,'w')
    f.write(before)
    f.close()

    f = open(after_name,'w')
    f.write(after)
    f.close()


def create_jsb(filename,before_name,after_name):
    create_before_after(APPJS_PATH,before_name,after_name)

    jsb = get_jsb(before_name,after_name)
    f = open(filename,'w')
    f.write(jsb)
    f.close()

if __name__ == '__main__':
    pass

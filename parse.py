#!/usr/bin/env python
#coding=utf-8

'''
@author: stonelee 
@email: istonelee@gmail.com
@blog: http://stonelee.info
@description: parse requires filenames form file

'''

import re

def parse_requires(data):
    '''
    data为文件内容
    如果有requires则返回数组,形如：
    ['CIIS.view.HeaderPanel', 'CIIS.view.SidebarPanel', 'CIIS.view.MainPanel', 'CIIS.view.FooterPanel']
    如果没有返回数组[]
    '''
    content = get_requires_content(data)
    if content:
        return get_filenames(content)
    else:
        return []

def get_requires_content(data):
    pattern = re.compile('requires\s*:\s*\[([^\]]+)\]')
    result = pattern.search(data)
    if result:
        return result.group(1)

def get_filenames(data):
    pattern = re.compile('\'([^\']*)\'')
    return re.findall(pattern,data)


def _test(filename,firstRequirefile,requiresNum):
    f = open('test/%s' %filename)
    data = f.read()
    results =  parse_requires(data)
    assert len(results) == requiresNum
    if results:
        assert results[0] == firstRequirefile

##############################
def close_autoload(data):
    #关闭动态依赖加载
    pattern = re.compile(r'(Ext.Loader.setConfig[\s\S]+enabled\s*:)[^,]+(,)')
    return pattern.sub(r'\1 false \2',data)

def split_appjs(data):
    #将app.js按Ext.application分成两部分
    pattern = re.compile(r'([\s\S]*)(Ext\.application[\s\S]*)')
    result = pattern.search(data)
    if result:
        return (result.group(1),result.group(2))
    else:
        return ('','')

if __name__ == '__main__':
    _test('requires_wrap.js','CIIS.view.constant.administrativeduty.List',8)
    _test('requires_oneline.js','CIIS.view.HeaderPanel',4)
    _test('requires_no.js','',0)

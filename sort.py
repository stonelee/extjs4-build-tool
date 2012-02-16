#!/usr/bin/env python
#coding=utf-8

'''
@author: stonelee 
@email: istonelee@gmail.com
@blog: http://stonelee.info
@description: sort based on requires
调用方法： sort_by_require(data), 其中data为表示依赖关系的dict
返回按照依赖关系排列的数组
'''

def sort_by_require(data):
    def sort(key,data):
        if key not in results:
            for value in data[key]:
                if value not in results:
                    if value in data.keys():
                        sort(value,data)
                    else:
                        results.append(value)
            results.append(key)

    results = []
    for key in data:
        sort(key,data)

    return results

if __name__ == '__main__':
    requires = {'a':['b','c'],'c':['d','e'],'f':['a','c']}
    assert sort_by_require(requires) == ['b', 'd', 'e', 'c', 'a', 'f']

    requires = {'h':[],'a':['b','c'],'c':['d','e'],'f':['a','c'],'g':[]}
    #如果没有依赖关系则没有固定次序
    assert sort_by_require(requires) == ['b', 'd', 'e', 'c', 'a', 'h', 'g', 'f']


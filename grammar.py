# -*- coding: utf-8 -*-

"""
  基础语法整理类
"""
class Grammar:

    def __init__(self):
      pass

    def f_array(self):
      days = [1,2,3,3,4,5]
      print '声明days:',days
      print 'days len(days) 长度为:',len(days)
      days.append(7)
      print 'days append(7):',days
      days.reverse()
      print 'days reverse():',days
      days.sort()
      print 'days sort():',days
      days.sort(reverse=True)
      print 'days sort(reverse=True):',days
      days.remove(7)
      print 'days remove(7):',days
      days.pop(1)  #pop 为index值，移除了days里面的2的值
      print 'days pop(1):',days
      days.pop()
      print 'days pop()移除最后一个元素:',days
      days.insert(1,10)
      print 'days insert(1,10) 插入元素:',days
      print 'days index(3) 元素 index:',days.index(3)
      print 'days count(3) 元素3出现的次数:',days.count(3)
      print 'days max value:',max(days),',min value:',min(days)
      
      print '交集：list(set(array1) & set(array2))'



if __name__ == '__main__':
  Grammar().f_array()


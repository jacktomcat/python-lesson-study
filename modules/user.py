# -*- coding: utf-8 -*-
from employee import Employee

#继承关系，可以多继承  User(Employee,Parent)
class User(Employee):

  def __init__(self, id, email, username):
    self.id = id
    self.email = email
    self.username = username

  #调用本类的方法和调用父类的方法
  def getNames(self):
    print ("子类调用父类方法...",self.getList(),self.shows(),"........")

  def getList(self):
    return "getList 方法调用..."

  """重写父类shows方法"""
  def shows(self):
      return "children instance method shows"
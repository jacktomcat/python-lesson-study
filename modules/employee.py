
class Employee:

  #实例方法带参数  employee().shows()
  def shows(self):
      return "instance method shows"

  #类方法带参数   employee.times()
  @classmethod
  def times(cls):
      return "class method times"

  #类方法不带参数   employee.names()
  @staticmethod
  def names():
      return "static method names"
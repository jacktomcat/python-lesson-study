# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify,json
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] ='jackjboss'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://upenv:upenv@localhost:3306/accelarator' #这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名text1
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True #设置这一项是每次请求结束后都会自动提交数据库中的变动
db = SQLAlchemy(app)

@app.route('/roles/getRoles')
def getRoles():
  json_roles=[]
  roles = Role.query.all()
  for role in roles:
    r = {"id":role.id,"name":role.name}
    json_roles.append(r)
    print "ID=",role.id,",姓名=",role.name
  return jsonify(json_roles) 

"""这里展示
      1:按id查询
"""
@app.route('/roles/<int:id>')
def getRoleById(id):
  role = Role.query.get(id)
  r = {"id":role.id,"name":role.name}
  print "ID=",role.id,",姓名=",role.name
  return jsonify(r)

"""这里展示
      1:除了id之外的字段进行查询
      2:字符串格式化 '%s' %(xx)
      3:'{}{}'格式化
      4: if else的判断操作
"""
@app.route('/roles/<name>')
def getRoleByName(name):
  role = Role.query.filter_by(name=name).first()
  if role == None:
    return 'no resource found by: %s, try %s !' %(name,'guest')
  else:
    r = {"id":role.id,"name":role.name}
    print 'ID={},姓名＝{}'.format(role.id, role.name)
    return jsonify(r)


@app.route('/roles/save')
def save():
  role = Role(id=7,name='jacktomcat')
  db.session.add(role)
  db.session.commit()

  r = {"id":role.id,"name":role.name}
  print 'ID={},姓名＝{}'.format(role.id, role.name)
  return jsonify(r)

@app.route('/roles/delete/<int:id>')
def delete(id):
  role = Role.query.get(id)
  db.session.delete(role)
  db.session.commit()
  return jsonify({"id":id})

@app.route('/roles/update/<int:id>')
def update(id):
  role = Role.query.get(id)
  role.name = '张三'
  db.session.add(role)
  db.session.commit()
  r = {"id":role.id,"name":role.name}
  return jsonify(r)


class Role(db.Model):
      __tablename__ = 'roles'
      id = db.Column(db.Integer,primary_key=True)
      name = db.Column(db.String(64),unique=True)
     #user = db.relationship('User',backref='role',lazy='dynamic')#建立两表之间的关系，其中backref是定义反向关系，lazy是禁止自动执行查询（什么鬼？）

    # def __repr__(self):
    #  return '<Role {}> '.format(self.name)
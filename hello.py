from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify,json
from user import User
from flask_sqlalchemy import SQLAlchemy
from modules.employee import Employee

app = Flask(__name__)
app.config['SECRET_KEY'] ='jackjboss'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://upenv:upenv@localhost:3306/accelarator' #这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名text1
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True #设置这一项是每次请求结束后都会自动提交数据库中的变动
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/get/<name>', methods=['GET', 'POST'])
def get(name):
    if request.method == 'POST':
      return render_template('hello.html', name=name)
    else:
      #return redirect(url_for('index'))
      return redirect("http://www.baidu.com", code=302)
      #return 'User %s' % name

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

@app.route('/api/getUser')
def get_current_user():
    tasks = []
    """user = User(1,'zhuhh','jackjboss@163.com')
    user1 = User(2,'zhuhh2','jackjboss2@163.com')
    user2 = User(3,'zhuhh3','jackjboss3@163.com')"""

    user={"id":1,"email":"jackjboss1@163.com","name":"zhuhh1"}
    user1={"id":2,"email":"jackjboss2@163.com","name":"zhuhh2"}
    user2={"id":3,"email":"jackjboss3@163.com","name":"zhuhh3"}

    tasks.append(user)
    tasks.append(user1)
    tasks.append(user2)
    """return jsonify(username='zhuhh',
                   email='jackjboss@163.com',
                   id=1)"""
    return jsonify(tasks)
    #return json.dumps(tasks)          
@app.route('/roles/getRoles')
def getRoles():
  Role.query.all()
  return 'get roles'


class Role(db.Model):
     __tablename__ = 'roles'
     id = db.Column(db.Integer,primary_key=True)
     name = db.Column(db.String(64),unique=True)
     #user = db.relationship('User',backref='role',lazy='dynamic')#建立两表之间的关系，其中backref是定义反向关系，lazy是禁止自动执行查询（什么鬼？）

     def __repr__(self):
      return '<Role {}> '.format(self.name)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
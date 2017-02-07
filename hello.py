from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify,json
from User import User

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(port=5000, debug=True)
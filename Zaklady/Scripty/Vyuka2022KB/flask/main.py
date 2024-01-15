from flask import Flask, render_template
app = Flask(__name__)


posts=[
        {'post_id':1,
        'title':'Titulek',
        'created':'18.3.2021',
        'content':'Obsah tohoto příspěvku'},
        {'post_id':2,
        'title':'Titulek2',
        'created':'18.3.2021',
        'content':'Obsah druhého příspěvku'}
    ]

def get_post(id):
    for post in posts:
        if post['post_id']==id:
            return post

@app.route('/hello-world')
def hello_world(name:str, adresa:int)->str:
    return "Hello world"

@app.route('/')
def index():
    return render_template('index.html',posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    print(post)
    return render_template('post.html', post=post)

@app.route('/hello')
def hello():
    return r'<h1>Hello</h1>'


if __name__ == '__main__':
    app.run()
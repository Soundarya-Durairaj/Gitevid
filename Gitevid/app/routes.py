from flask import render_template, redirect, url_for
from app import app

@app.route('/')
def index():
    posts = [
        {'id': 1, 'title': 'First Post'},
        {'id': 2, 'title': 'Second Post'}
    ]
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    posts = [
        {'id': 1, 'title': 'First Post', 'summary': 'Summary of first post'},
        {'id': 2, 'title': 'Second Post', 'summary': 'Summary of second post'}
    ]
    return render_template('blog.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = {'id': post_id, 'title': f'Post {post_id}', 'content': f'Full content of post {post_id}.'}
    return render_template('post_detail.html', post=post)


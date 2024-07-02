from flask import Flask, render_template
from requests import get
from post import Post

API_LINK = 'https://api.npoint.io/1a770340ef2283d5a6d9'

app = Flask(__name__)

all_posts = get(API_LINK).json()
post_list = []
for post in all_posts:
    post_list.append(Post(post["id"], post["title"], post["subtitle"], post["body"]))


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index:int):
    post = None
    for blog_post in post_list:
        if index == blog_post.id:
            post = blog_post
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)

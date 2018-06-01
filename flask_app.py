
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

all_articles = Articles()

app.debug = True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles=all_articles)


@app.route('/article/<string:id>')
def article(id):
    return render_template('article.html', id=id)

#if __name__ == "__main__":
#    app.run()

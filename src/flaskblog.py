from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author'     : 'Mateus da Fonte',
        'title'      : 'Blog Post 1',
        'content'    : 'First post content',
        'date_posted': 'April 20, 2018'
    },
        {
        'author'     : 'Julinho Babalu',
        'title'      : 'Blog Post 2',
        'content'    : 'Second post content',
        'date_posted': 'May 20, 2018'
    },
        {
        'author'     : 'Juan Carlos',
        'title'      : 'Blog Post 3',
        'content'    : 'Third post content',
        'date_posted': 'January 20, 2018'
    }
]

@app.route("/")                         # route anotation/decorator
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")                         # route anotation/decorator
def about():
    return render_template("about.html",title='About')
if __name__ == "__main__":
    app.run(debug=True)
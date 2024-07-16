from flask import Flask


app = Flask(__name__)

def make_bold(func):
    def wrapper(*args, **kwargs):
        print('(<b>{func}</b>)')
    return wrapper


@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center"> Hello, World!</h1> '
            '<p>This is a paragraph</p>'
            '<img src="https://nz.rs-cdn.com/images/nwsp9-jl7cn/blog/156b483391b278de9c96bb02b9a61712__980a/zoom668x398z101000cw668.jpg" >')


@app.route("/bye")
@make_bold
def bye():
    return "Bye"


@app.route("/user/<name>")
def hello(name):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run(debug=True)

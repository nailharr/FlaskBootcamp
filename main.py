from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def main():
#     return "<h1>Hello, world!</h1><br><a href='/index'>2st page</a>"\

@app.route('/')
def main():
    variable = "placeholder was here"
    return render_template("main_page.html", placeholder=variable)


@app.route('/calc/<x>/<y>')
def calc(x, y):
    return f"<h2>Result:</h2> {int(x) + int(y)} <br><a href='/'>Go to main page</a>"

# TODO: add table parsing
@app.route('/table')
def table():
    with open("files_in/peoples_data.csv", "r", encoding="utf8") as file:
        print(file.read())
    return render_template("table_peoples.html")

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template
from flask import render_template, flash, redirect, request, url_for

app = Flask(__name__)


@app.route('/')
def main():
    variable = "placeholder was here"
    return render_template("main_page.html", placeholder=variable)


@app.route('/plus/<x>/<y>')
def plus(x, y):
    return f'<h2>Result:</h2> {int(x) + int(y)} <br><br>' \
           f'<button type="button">' \
           f'<a href="/">Go to main page</a>' \
           f'</button>'


@app.route('/table')
def table():
    with open("files_in/peoples_data.csv", "r", encoding="utf8") as file:
        people_data = list()
        for line in file.readlines():
            people_data.append(tuple(line.split('\n')[0].split(',')))

        # print(people_data)

    return render_template("table_peoples.html", data=people_data)


if __name__ == '__main__':
    app.run()

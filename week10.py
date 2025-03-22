from flask import Flask

app = Flask(__name__)

@app.route('/index/<string:name>/<int:age>')
def index(name, age):
    # url = url_for('get_text')
    return """
    <html>
        <head>
            <title>Simple Flask App</title>
        </head>
        <body>
            <h1>Index page</h1>
            <p>Hello {}!</p>
            <p> You are {} years old.</p>
            <hr>
            <a href="{}">Welcome</a>
        </body>
    </html>
    """.format(name, age,)




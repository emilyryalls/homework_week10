from flask import Flask, url_for
app = Flask(__name__)


# a welcome page with a dynamic route
@app.route('/welcome/<string:name>')
def welcome_page(name):
    return f"Welcome {name.title()} to the homepage"


# an about us page linking to individual pages
@app.route('/about')
def about_us():
    url = url_for('about_emily')
    url2 = url_for('about_ivon')
    url3 = url_for('about_anna')
    url4 = url_for('about_ayishat')
    url5 = url_for('about_malvina')
    return """
    <html>
        <head>
            <title>About Us</title>
        </head>
        <body>
            <h1>This is the About Us Page</h1>
            <p>We are group 1 from the Get Into Tech Program Cohort 1</p>
            <p>See links to individual pages below</p><br>   
            <a href="{}">Emily's page</a><br>
            <a href="{}">Ivon's page</a><br>
            <a href="{}">Anna's page</a><br>
            <a href="{}">Ayishat's page</a><br>
            <a href="{}">Malvina's page</a>
        </body>
    </html>

    """.format(url, url2, url3, url4, url5)

@app.route('/about/emily')
def about_emily():
    return """
    <html>
        <head>
            <title>About Emily</title>
        </head>
        <body>
            <h1>About Emily</h1>
            <p>Placeholder</p>
            <hr>
        </body>
    </html>
    """.format()
# add anchor tag to click back to home page

@app.route('/about/ivon')
def about_ivon():
    return """
    <html>
        <head>
            <title>About Ivon</title>
        </head>
        <body>
            <h1>About Ivon</h1>
            <p>Placeholder</p>
            <hr>
        </body>
    </html>
    """.format()

@app.route('/about/anna')
def about_anna():
    return """
    <html>
        <head>
            <title>About Anna</title>
        </head>
        <body>
            <h1>About Anna</h1>
            <p>Placeholder</p>
            <hr>
        </body>
    </html>
    """.format()

@app.route('/about/ayishat')
def about_ayishat():
    return """
    <html>
        <head>
            <title>About Ayishat</title>
        </head>
        <body>
            <h1>About Ayishat</h1>
            <p>Placeholder</p>
            <hr>
        </body>
    </html>
    """.format()

@app.route('/about/malvina')
def about_malvina():
    return """
    <html>
        <head>
            <title>About Malvina</title>
        </head>
        <body>
            <h1>About Malvina</h1>
            <p>Placeholder</p>
            <hr>
        </body>
    </html>
    """.format()


if __name__ == "__main__":
    app.run(port=5001, debug=True)
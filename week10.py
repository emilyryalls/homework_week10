from flask import Flask, url_for

app = Flask(__name__)

# we have created a welcome page
@app.route('/welcome')
def welcome_page():
    return "Welcome to the home page"


# we created an about us page linking back to the welcome page showing a dynamic route
@app.route('/about/<name>')
def about_us(name):
    url = url_for('welcome_page')
    return """
    <html>
        <head>
            <title>About Us</title>
        </head>
        <body>
            <h1>This is the About Us Page</h1>
            <p>We are group 1 from the Get Into Tech Program Cohort 1</p>
            <p>This is a link to <a href="{}">our welcome page</a> </p>
            <p> {} has her own separate page </p>     
        </body>
    </html>
    
    """.format(url, name)



if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/index/<string:name>/<int:age>')
# def index(name, age):
#     # url = url_for('get_text')
#     return """
#     <html>
#         <head>
#             <title>Simple Flask App</title>
#         </head>
#         <body>
#             <h1>Index page</h1>
#             <p>Hello {}!</p>
#             <p> You are {} years old.</p>
#             <hr>
#             <a href="{}">Welcome</a>
#         </body>
#     </html>
#     """.format(name, age,)




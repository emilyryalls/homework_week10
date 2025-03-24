from doctest import debug

from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/ivon')
def ivon():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="static/style.css" type="text/css">
            <title>Ivon's Page</title>
        </head>
        <body>
            Hi!! This is Ivon
        </body>
        </html>
    """


@app.route('/anna')
def anna():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="static/style.css" type="text/css">         
            <title>Anna's Page</title>
        </head>
        <body>
            Hi!! This is Anna
        </body>
        </html>
    """


@app.route('/emily')
def emily():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="static/style.css" type="text/css">            
            <title>Emily's Page</title>
        </head>
        <body>
            Hi!! This is Emily
        </body>
        </html>
    """


@app.route('/malvina')
def malvina():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="static/style.css" type="text/css">            
            <title>Malvina's Page</title>
        </head>
        <body>
            Hi!! This is Malvina
        </body>
        </html>
    """


@app.route('/ayishat')
def ayishat():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="static/style.css" type="text/css">            
            <title>Ayishat's Page</title>
        </head>
        <body>
            Hi!! This is Ayishat
        </body>
        </html>
    """


@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get('input_data')
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="static/style.css" type="text/css">            
            <title>Submit Page</title>
        </head>
        <body>
            Thank you for the following message: {}
        </body>
        </html>
    """.format(data)


@app.route('/indexhomework')
def indexhomework():
    url_ivon = url_for('ivon')
    url_anna = url_for('anna')
    url_emily = url_for('emily')
    url_malvina = url_for('malvina')
    url_ayishat = url_for('ayishat')

    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <!-- Required meta tags -->
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
            <!-- Style Sheet -->
            <link rel="stylesheet" href="static/style.css" type="text/css">

            <title>Group One Page</title>
        </head>
        <body>
            <div class="container">
                <header class="d-flex flex-wrap justify-content-center py-3 mb-5">
                  <a href="#" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none">
                    <!-- <svg class="bi me-2" width="40" height="32"><use xlink:href="#"/></svg> -->
                    <span class="fs-4" aria-current="page">Group one</span>
                  </a>

                  <ul class="nav nav-pills">
                    <li class="nav-item"><a href="{}" class="nav-link text-body" >Ivon</a></li>
                    <li class="nav-item"><a href="{}" class="nav-link text-body">Anna</a></li>
                    <li class="nav-item"><a href="{}" class="nav-link text-body">Emily</a></li>
                    <li class="nav-item"><a href="{}" class="nav-link text-body">Malvina</a></li>
                    <li class="nav-item"><a href="{}" class="nav-link text-body">Ayishat</a></li>
                  </ul>
                </header>
            </div>

            <section class="container-fluid bg-1 text-center">
                <h1>Welcome to our presentation page</h1>
                <p>Please select a name on the Navigation Menu above to learn about each of us</p>
            </section>

            <section class="container-fluid bg-2 text-center">
                <h1>What have we learned</h1>
                <div class="row justify-content-center">
                    <div class="col-sm-4">
                        <p>HTML</p>
                    </div>
                    <div class="col-sm-4">
                        <p>CSS</p>
                    </div>
                    <div class="col-sm-4">
                        <p>BOOTSTRAP</p>
                    </div>
                </div>
                <div class="row justify-content-center">
                    <div class="col-sm-4">
                        <p>JS</p>
                    </div>
                    <div class="col-sm-4">
                        <p>GIT</p>
                    </div>
                    <div class="col-sm-4">
                        <p>PYTHON</p>
                    </div>
                </div>
                <div class="row justify-content-center">
                    <div class="col-sm-4">
                        <p>MYSQL</p>
                    </div>
                    <div class="col-sm-4">
                        <p>FLASK</p>
                    </div>
                </div>
            </section>

            <section class="container-fluid bg-3 text-center">
                <h1>Let's get in touch! Say Hello!</h1>
                <form method="POST" action="/submit">
                    <input type="text" name="input_data" placeholder="Enter some data">
                    <button type="submit">Submit</button>
                </form>
            </section>

            <footer class="bg-4 text-center">
                <p>&copy; 2025 Created by GIT Group One <a href=#></a></p>
            </footer>

            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        </body>
        </html>
    """.format(url_ivon, url_anna, url_emily, url_malvina, url_ayishat)


if __name__ == "__main__":
    app.run(debug=True)
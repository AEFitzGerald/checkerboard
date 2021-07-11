from flask import Flask, render_template
app = Flask(__name__)


#1. Display an 8 x 8 checkerboard
@app.route('/')
def checkerboard_eight():
    return render_template('index.html', x = int(8))

# #2. Display a 8 by 4 checkerboard
@app.route('/4')
def checkerboard_four():
    return render_template('index.html', x = int(8), y = int(4))

@app.route('/<int:x>/<int:y>')
def checkers_random(x=int(),y=int()):
    return render_template('index.html', x = x, y = y)


if __name__=="__main__":
    app.run(debug=True)



# @app.route('/<int:x>/<int:y>')
# def checkers_random(x, y):
#             return render_template('index.html', x = x, y = y, checkers_dark = checkers_dark, checkers_light = checkers_light, checkerboard = checkerboard)


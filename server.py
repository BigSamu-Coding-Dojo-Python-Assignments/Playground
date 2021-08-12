from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def normal_checkboard():
    return render_template('index.html', num_rows=8, num_cols=8)

@app.route('/<x>')
def sized_checkboard(x):
    return render_template('index.html', num_rows=int(x), num_cols=int(x))

@app.route('/<x>/<y>')
def sized_checkboard_two_dimensions(x, y):
    return render_template('index.html', num_rows=int(x), num_cols=int(y))

@app.route('/<x>/<y>/<c1>/<c2>')
def sized_checkboard_two_dimensions_and_color(x, y, c1, c2):
    return render_template('index.html', num_rows=int(x), num_cols=int(y), color1=c1, color2=c2)

if __name__=="__main__":
    app.run(debug=True)
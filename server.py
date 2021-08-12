from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/play')                           
def play_level_one():
    return render_template('index.html', num_times=3)

@app.route('/play/<num>')                           
def play_level_two(num):
    return render_template('index.html', num_times=int(num)) 

@app.route('/play/<num>/<color>')                           
def play_level_three(num,color):
    return render_template('index.html', num_times=int(num), color=color) 
    
if __name__=="__main__":
    app.run(debug=True)     
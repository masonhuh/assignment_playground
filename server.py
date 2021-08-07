from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Playground Assingment! "/play" for Level 1'

@app.route('/play/<int:num>')
def bluebox(num):
    return render_template('play.html',num=num,)

@app.route('/play/<int:num>/<string:color>')
def play(num, color):
    return render_template('play.html',num=num,color=color)

if __name__=="__main__":
    app.run(debug=True)
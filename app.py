from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/input')
def input():
   return render_template('input.html')

@app.route('/board')
def home():
   return render_template('modify.html')
#
# @app.route('/join')
# def home():
#    return render_template('join.html')
#
# @app.route('/login')
# def home():
#    return render_template('login.html')

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
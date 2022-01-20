from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/dbsparta"
mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/input', methods=["GET","POST"])
def input():
    if request.method == "POST":
        user_name = request.form.get("name")
        user_pw = request.form.get("pw")
        user_content = request.form.get("content")
        # current_utc = round(datetime.utcnow().timestamp() * 1000)
        # print(user_name, current_utc)
        print(user_name)

        data = mongo.db.userinput
        post = {
            "name": user_name,
            "PW": user_pw,
            "content": user_content,
            # "utc_stamp": current_utc
        }
        data.insert_one(post)
        return render_template('board.html')
    else:
        return render_template('input.html')

@app.route('/board')
def board_page():
    return render_template('board.html')

@app.route('/board_data', methods=['GET'])
def board():
    userinput = list(mongo.db.userinput.find({}, {'_id': False}))
    return jsonify({'all_input': userinput})

@app.route('/join')
def join():
    return render_template('join.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

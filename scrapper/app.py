from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")     #바꾸면 새롭게 들어가야함 터미널에서 ctrl +c 하고 다시
@app.route('/search')
def search():
    return render_template("search.html")
if __name__ == '__main__':
    app.run(debug=True)   #debug=True 개발자 모드 => 자동으로 서버가 저장
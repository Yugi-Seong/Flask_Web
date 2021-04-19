from flask import Flask , render_template


app = Flask(__name__) # 내장변수를 이용해 Flask 객체 생성 

app.debug = True #오류가 생길 경우 웹페이지 상에서 띄워 줌 => 개발 후 False로 변경 또는 없애주기

#데코레이터 @
@app.route('/', methods =['GET']) #요청을 받았을때 라우팅 파일을 호출  
def index() : # 함수로 처리
    # return "Hello World"
    return render_template("index.html", data = "Seong") #render_template는  html문서를 인자값으로 받아 문서를 해석하여 document type 으로 변경하여 요청한 곳으로 보내줌 

@app.route('/about')
def about():
    return render_template("about.html", hello = "Yugi Seong")

@app.route('/articles')
def articles():
    return render_template("articles.html", hello = "Yugi Seong")

if __name__ == '__main__' : #app.py에서 이 부분을 가장 먼저 실행함! / 서버 띄우는 곳에 적어줌
    app.run()


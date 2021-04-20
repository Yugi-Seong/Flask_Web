from flask import Flask , render_template, request, redirect 
from data import Articles
import pymysql

app = Flask(__name__) # 내장변수를 이용해 Flask 객체 생성 

app.debug = True #오류가 생길 경우 웹페이지 상에서 띄워 줌 => 개발 후 False로 변경 또는 없애주기

db = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '1234',
    db = 'busan'
)


#데코레이터 @
@app.route('/', methods =['GET']) #요청을 받았을때 라우팅 파일을 호출  
def index() : # 함수로 처리
    # return "Hello World"
    return render_template("index.html", data = "Yugi Seong") #render_template는  html문서를 인자값으로 받아 문서를 해석하여 document type 으로 변경하여 요청한 곳으로 보내줌 

@app.route('/about')
def about():
    return render_template("about.html", data= "Yugi Seong")

@app.route('/articles')
def articles():
    cursor = db.cursor()
    sql = 'SELECT * FROM topic ;'
    cursor.execute(sql)
    topics = cursor.fetchall()
    print(topics)
    # articles = Articles()
    # print(articles[0]['title']) #consol 창에 나타남 
    return render_template("articles.html", articles = topics)

@app.route('/article/<int:id>') #params 로 이용하기 : <변수명> 으로 적어줌 
def article(id) :
    cursor = db.cursor()
    sql = 'SELECT * FROM topic WHERE id = {}'.format(id)
    cursor.execute(sql)
    topic = cursor.fetchone()
    print(topic)
    # articles = Articles()
    # article = articles[id-1]
    # print(articles[id-1])
    return render_template("article.html", article = topic)

@app.route('/add_articles', methods = ["GET","POST"])
def add_articles():
    cursor = db.cursor()
    if request.method == "POST" :  # form을 이용해서 submit을 하는 형태 ('POST')방식
        author = request.form['author']
        print(request.form['author'])
        title = request.form['title']
        print(request.form['title'])
        desc = request.form['desc']
        print(request.form['desc'])

        sql = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
        input_data = [title,desc,author]

        cursor.execute(sql, input_data)
        db.commit()
        print(cursor.rowcount)
        # db.close()
        return redirect("/articles")

    else :
        return render_template("add_articles.html") #주소창에 /add_articles 입력할 경우('GET'방식)

    
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cursor = db.cursor()
    sql = 'DELETE FROM topic WHERE id = %s ;'
    id = [id]
    cursor.execute(sql, id)

    # sql = 'DELETE FROM topic WHERE id = {};'.format(id)
    # cursor.execute(sql)
    db.commit()
    return redirect("/articles")


if __name__ == '__main__' : #app.py에서 이 부분을 가장 먼저 실행함! / 서버 띄우는 곳에 적어줌
    app.run()


from flask import Flask , render_template, request, redirect 
from data import Articles
import pymysql
from passlib.hash import sha256_crypt


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
    cursor.execute(sql) #sql 쿼리 실행 
    topics = cursor.fetchall()
    # print(topics)
    # articles = Articles()
    # print(articles[0]['title']) #consol 창에 나타남 
    return render_template("articles.html", articles = topics)

@app.route('/article/<int:id>') #params 로 이용하기 : <변수명> 으로 적어줌 
def article(id) :
    cursor = db.cursor()
    sql = 'SELECT * FROM topic WHERE id = {}'.format(id)
    cursor.execute(sql)
    topic = cursor.fetchone()
    # print(topic)

    # articles = Articles()
    # article = articles[id-1]
    # print(articles[id-1])
    return render_template("article.html", article = topic)

@app.route('/add_articles', methods = ["GET","POST"])
def add_articles():
    cursor = db.cursor()
    if request.method == "POST" :  # form을 이용해서 submit을 하는 형태 ('POST')방식
        author = request.form['author']
        title = request.form['title']
        desc = request.form['desc']
       

        sql = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
        input_data = [title,desc,author]

        cursor.execute(sql, input_data)
        db.commit()
        # print(cursor.rowcount)
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


#articles글 수정하기 
@app.route('/<int:id>/edit', methods=["GET","POST"])
def edit(id) :
    cursor = db.cursor()

    if request.method == "POST" :
        title = request.form['title']
        desc = request.form['desc']
        author = request.form['author']
        print(author)
        # print(request.form['title'])
        sql = ' UPDATE topic SET title = %s, body = %s, author = %s WHERE id = {};'.format(id)
        input_data = [title, desc,author]
        cursor.execute(sql, input_data)
        db.commit()
        return redirect('/articles')
        # f'SELECT * FROM topic WHERE id={id};'

    else :
        sql = "SELECT * FROM topic WHERE id = {}".format(id)
        cursor.execute(sql)
        topic = cursor.fetchone()
        # print(topic[1]) 
        return render_template("edit_article.html", article = topic)

# 회원가입
@app.route("/register", methods = ["GET","POST"])
def register():
    cursor = db.cursor()

    if request.method == "POST" : 
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = sha256_crypt.encrypt(request.form['password'])
        sql = "INSERT INTO `users` (`name`, `email`, `username`, `password`) VALUES (%s,%s,%s,%s);"
        input_data = [name,email,username,password]
        cursor.execute(sql, input_data)
        db.commit()
        # return "Success"
        return redirect("/")

    else :
        return render_template("register.html")

#로그인
@app.route('/login', methods=['GET','POST'])
def login():
    cursor = db.cursor()

    if request.method == "POST" :

        email = request.form['email']   #login.html 에서 name = email 로 받아오면 여기 부분에서 email 로 받기 
        password_1 = request.form['password']
        # print(username)
        # print(password_1)

        #db에서 비밀번호 조회
        sql =  'SELECT * FROM users WHERE email = %s ;'
        input_data = [email]
        cursor.execute(sql,input_data)
        user = cursor.fetchone()

        if user == None :  #ID가 존재하지 않을 경우 
            print(user)
            return redirect('/register')
        else :
            if sha256_crypt.verify(password_1, user[4]) : 
                return redirect('/articles')
            else : 
                return user[4]
    else :
        return render_template('login.html')

        
         

      



if __name__ == '__main__' : #app.py에서 이 부분을 가장 먼저 실행함! / 서버 띄우는 곳에 적어줌
    app.run()


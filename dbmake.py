import pymysql

db = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '1234',
    db = 'busan'
)

sql = '''
    CREATE TABLE `topic` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `title` varchar(100) NOT NULL,
        `body` text NOT NULL,
        `author` varchar(30) NOT NULL,
        `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id)
	) ENGINE=innoDB DEFAULT CHARSET=utf8;
'''

# cursor 메소드 사용 하여 cursor 인스턴스 생성   
# cursor = db.cursor()

# cursor.execute('SELECT * FROM users ;')

#조회한 내용을 fetchall 메소드로 모두 받아와 users table(클라이언트) 에 저장  
# users = cursor.fetchall()
# print(users)

# cursor = db.cursor()
# cursor.execute(sql)   #python에서 조회
# db.commit()
# db.close()



# sql_3  = '''
# INSERT INTO `busan`.`users` 
# (`name`, `email`, `username`, `password`) 
# VALUES 
# ('성유기2', 'tjddbrl2@naver.com', 'SeongYugi2', '123456');
# '''


# cursor = db.cursor()
# cursor.execute(sql_3)
# db.commit()
# db.close()


# cursor = db.cursor()
# cursor.execute('SELECT * FROM users ;')
# users = cursor.fetchall()
# print(users)



# sql_3 = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
# title = input('제목을 적으세요')
# body = input("내용을 적으세요")
# author = input("누구세요?")
# input_data = [title,body,author ]
# cursor = db.cursor()
# cursor.execute(sql_3,input_data)
# db.commit()
# db.close()


cursor = db.cursor()
cursor.execute('SELECT * FROM topic ;')
users = cursor.fetchall()
print(users)

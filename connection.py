import mysql.connector

def create_db():
    try:
        con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="inshort_bharat"
        )
        print("Connection Success")
    except Exception as e:
        print(e)

    cursor=con.cursor()
    
    cursor.execute('''CREATE TABLE users (id INT AUTO_INCREMENT,  
                   name VARCHAR(255) NOT NULL,  
                   email VARCHAR(255) NOT NULL,  
                   password VARCHAR(255) NOT NULL,  
                   type VARCHAR(255) NOT NULL,  
                   image_url VARCHAR(255), 
                   PRIMARY KEY (id)); ''')
    con.commit()

    cursor.execute('''CREATE TABLE news (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    image VARCHAR(255) NOT NULL,
    slug VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    tags VARCHAR(255) NOT NULL,
    published_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    published_by VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL); ''')
    con.commit()

    cursor.execute('''CREATE TABLE favorites (
    id INT NOT NULL AUTO_INCREMENT,
    post_id INT NOT NULL,
    user_id INT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (post_id) REFERENCES news(id),
    FOREIGN KEY (user_id) REFERENCES users(id));''')
    con.commit()

    cursor.execute('''CREATE TABLE readlater (
    id INT PRIMARY KEY AUTO_INCREMENT,
    post_id INT NOT NULL,
    user_id INT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP); ''')
    con.commit()

    cursor.execute('''CREATE TABLE comments (
  id INT AUTO_INCREMENT PRIMARY KEY,
  post_id INT NOT NULL,
  user_id INT NOT NULL,
  comment TEXT NOT NULL,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  sentiment VARCHAR(255) NOT NULL); ''')
    con.commit()

    cursor.execute('''CREATE TABLE social (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  facebook VARCHAR(255),
  instagram VARCHAR(255),
  twitter VARCHAR(255),
  linkedin VARCHAR(255),
  google VARCHAR(255),
  FOREIGN KEY (user_id) REFERENCES users(id)); ''')
    con.commit()

    cursor.execute("CREATE TABLE newsletter ( email VARCHAR(255) NOT NULL); ")
    con.commit()


    

create_db()
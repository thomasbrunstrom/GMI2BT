"""env FLASK_APP=flaskex.py FLASK_ENV=development flask run"""

from flask import Flask, escape, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adduser', methods=['GET'])
def adduser(data = None):
    #if data:
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT username, id FROM users')
    users = c.fetchall()
    nousers = len(users)
    return render_template('adduser.html', username=data, users=users, len = nousers) 
    #return render_template('adduser.html')

@app.route('/robert')
def robert():
    return 'Hej Robert, gillar du astroider?'

@app.route('/users')
def users():
    #Fixa så att vi hämtar från databasen
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT username, password, id FROM users')
    users = c.fetchall()
    return jsonify(users)

@app.route('/users/<id>', methods=['GET'])
def deluser(id):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    p = (id, )
    c.execute('DELETE FROM users WHERE id=?', p)
    conn.commit()
    
    return { 'status' : f'Delete row with id: {id}' }

@app.route('/user/', methods=['POST'])
def addUser():
    # conn = sqlite3.connect('example.db')
    # c = conn.cursor()
    # p = (id, )
    # c.execute('INSERT INTO users (username, password) VALUES(?,?)', p)
    # conn.commit()
    print(request.form)    
    return { 'status' : f'Added user with username: {request.form.get("username")}' }

@app.route('/postjson/', methods=['POST'])
def postjson():
    # conn = sqlite3.connect('example.db')
    # c = conn.cursor()
    # p = (id, )
    # c.execute('INSERT INTO users (username, password) VALUES(?,?)', p)
    # conn.commit()
    print(request.json)    
    return request.json

@app.route('/adduser', methods=['POST'])
def adduserpost():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
        (request.form.get('username'), request.form.get('password')
    ))
    conn.commit()
    print('adduserpost')
    return adduser(request.form.get('username'))
#!/usr/bin/python3
from flask import Flask,request,session,redirect, url_for,render_template
import datetime,json,os,random
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
      if not 'username' in session or not session['username'] in users:
        return "Нет имени пользователя!"
      return f(*args,**kwargs)
    return decorated_function
    
app = Flask(__name__) 
app.secret_key = "qweewqqweewq"

@app.route("/")
def index():
    if 'username' in session:
        return render_template("index_welcome.html",me=session['username'],messages=users[session['username']]['box'],users=users) #"Welcome to the club %s" % session['username']
    return render_template("index.html",number_of_users=len(users))
    
users = { 'admin': {'password':'123', 'box':[]} }
if os.path.exists("data.json"):
    print("loading json")
    users = json.load(open("data.json",'r'))
else:
    print("saving json")
    json.dump(users,open("data.json",'w'))
def reload():
    print("saving json")
    json.dump(users,open("data.json",'w'))

@app.route("/register")
def register():
     username = request.values['username']
     password = request.values['password']
     #return "Username:" + username + "\n" + "password:" + str(password)
     #print(username,password)
     if username in users:
        return render_template("index.html",message="Пользователь уже существует!")
     else:
        users[username] = dict(password=password,box=[])
        reload()
        return render_template("index.html",message="Регистрация нового пользователя!")

@app.route("/login",methods=['POST'])
def login():
     username = request.values['username']
     password = request.values['password']  
     if username in users:
        if users[username]['password'] == password:
           session['username'] = username
           return redirect("/")
        else:
            #del session['username']
            return render_template("index.html",message="Неправильный пароль!" )
     else:
        return render_template("index.html",message="Нет такого пользователя!" )
        
@app.route("/logout")
def logout():
     if 'username' in session:
        del session['username']
        return render_template("index.html",message="Произведен выход!" )
     return index()
      
@app.route("/listuser")
@login_required
def listuser():
     return ",".join(users)
         
@app.route("/send",methods=["POST"])
@login_required
def send():
     username = request.values['username']
     message = request.values['message']
     mes = dict(frm=session['username'],message=message,date=str(datetime.datetime.now()),idx=random.randint(1,65536000))
     users[username]['box'].append(mes)
     reload()
     return render_template("index_send.html",message="Сообщение отправлено!")
     #redirect("/")
     #render_template("index_welcome.html",message="Сообщение отправлено!",me=session['username'],messages=users[session['username']]['box'],users=users)
          
@app.route("/message/<message_idx>")
@login_required
def message(message_idx):
     meslist = users[session['username']]['box']
     for mes in meslist:
       if 'idx' in mes and mes['idx'] == int(message_idx):
           return "%s) %s:%s\n" % (mes['date'],mes['frm'],mes['message'])
     return "Нет такого сообщения"   
    
app.run(host="0.0.0.0",port=1234) 
  


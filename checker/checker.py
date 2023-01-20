#!/usr/bin/python3
import requests,random,re,sys
#url = "http://0.0.0.0:1234/"
if len(sys.argv)==1:
	print("No args")
	quit()
url=sys.argv[1]
s1=requests.Session()
r = s1.get(url)
if not "Регистрация/Вход" in r.text:
	print("Нет Регистрация/Вход")
	exit(101)
#print("Есть Регистрация/Вход")
u1,p1=str(random.randint(1,10000000)),str(random.randint(1,10000000))
u2,p2=str(random.randint(1,10000000)),str(random.randint(1,10000000))
s2=requests.Session()
def RegUser(s,username,password):
  r=s.get(url+"register",params={"username":username,"password":password})
  if not "Регистрация нового пользователя" in r.text:
    print("Не могу зарегестрироваться")
    exit(101)
def LoginUser(s,username,password):
	r=s.post(url+"login",data={"username":username,"password":password})
	if not ("Добро пожаловать %s!" %username) in r.text:
		print("Не могу войти")
		exit(101)
def Index(s):
	r=s.get(url+"/")
	return r.text
def Send(s,u,m):
	r=s.post(url+"send",data={"username":u,"message":m})
	if not "Сообщение отправлено!" in r.text:
		print("Cannot send message")
		exit(101)
RegUser(s1,u1,p1)		
RegUser(s2,u2,p2)	
LoginUser(s1,u1,p1)	
LoginUser(s2,u2,p2)		
res=Index(s1)
if not u2 in res or not u2 in res:
 print("Cannot find user on page")
 exit(101)
mes = str(random.randint(1,10000000))
Send(s1,u2,mes)
res = Index(s2)
ref = re.findall(r"\<a href\=\'([^']+)\'> \Посмотреть",res)
if len(ref) == 0:
	print("cannot find ref to message")
	exit(101)
ref=ref[0]
res=s2.get(url+ref)
#print(res.text)
if not mes in res.text:
	print("Cannot receive message")
	exit(101)
print("OK")	
exit(100)
 

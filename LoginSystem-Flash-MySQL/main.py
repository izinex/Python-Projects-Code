# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template, app, request, redirect
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(host="localhost", user="root", password="agentzer0", database="userinfo")

cursor = mydb.cursor()




@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/login_check', methods=['POST', 'GET'])
def login_check():
    username = request.form.get('username')
    password = request.form.get('password')

    cursor.execute("""SELECT * FROM `users` WHERE `username` LIKE '{}' AND `password` LIKE '{}'"""
                   .format(username, password))
    users = cursor.fetchall()

    if len(users) > 0:
        redirect('/home')
    else:
        redirect('/')

    print(users)
    return 'Login Successful'


@app.route('/add_user', methods=['POST'])
def add_user():

    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    cursor.execute("""INSERT INTO `users` (`email`, `username`, `password`) VALUES ('{}','{}','{}')""".format(email,username,password))
    mydb.commit()
    return "User has been registered successfully"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

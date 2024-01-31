from flask import Flask ,render_template,request,json,jsonify,redirect,session
import os
from werkzeug.security import check_password_hash

import mysql.connector
from mysql_conn import create_user

app =Flask(__name__,template_folder="templates")

app.secret_key=os.urandom(25)


def mysql_con():
    conn=mysql.connector.connect(
        user = "root", password = "Sourav@1234",
        database="regform"
    )
    cursor=conn.cursor()
    return conn,cursor


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def sign_up():
    return render_template('signup.html')

@app.route("/home")
def home():
    if 'user_id' in session:
        return render_template("homepage.html")
    else:
        return redirect("/signin")


@app.route('/signin')
def showSignin():
    return render_template('signin.html')



@app.route("/api/signup" ,methods=['POST'])
def create():
    _name = request.form.get('inputName')
    _email = request.form.get('inputEmail')
    _password = request.form.get('inputPassword')

    conn, cursor = mysql_con()
    result = create_user(conn, cursor, _name, _email, _password)
    
    cursor.close()
    conn.close()

    # return jsonify({'message': result})
    return redirect("/signin")


@app.route("/api/validateLogin", methods=['POST'])
def check():
    _email=request.form.get("_inputEmail")
    _password=request.form.get("_inputPassword")

    conn, cursor = mysql_con()
    print("Input Email:", _email)
    print("Input Password:", _password)
    cursor.execute("SELECT * FROM tbl_user WHERE user_username LIKE %s AND user_password LIKE %s", (_email, _password))
    
    user= cursor.fetchone()
    print(user)
    if len(user) > 0:
        session['user_id'] = user[0]
        return redirect("/home")
    else:
        return redirect("/signin")




if __name__ == "__main__":
    app.run(debug=True)
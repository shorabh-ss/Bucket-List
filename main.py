from flask import Flask ,render_template,request,json,jsonify,redirect

import mysql.connector
from mysql_conn import create_user

app =Flask(__name__,template_folder="templates")


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







if __name__ == "__main__":
    app.run(debug=True)
import mysql.connector                 

def create_user(conn, cursor, p_name, p_username, p_password):
    cursor.execute("SELECT 1 FROM tbl_user WHERE user_username = %s", (p_username,))
    user_exists = cursor.fetchone()

    if user_exists:
        return 'Username Exists !!'
    else:
        cursor.execute("INSERT INTO tbl_user (user_name, user_username, user_password) VALUES (%s, %s, %s)",
                       (p_name, p_username, p_password))
        conn.commit()
        return 'User created successfully'
    




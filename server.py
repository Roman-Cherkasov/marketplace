import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect, jsonify
import json

app = Flask(__name__)


def get_db_connection():
# authentication
    conn = psycopg2.connect(host='localhost',
                            database='marketplace',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn

#  main page
@app.route('/get_user_data')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * from main.USERS\
                WHERE login = 'darth_vaider';")
    result_set = cur.fetchall()
    cur.close()
    conn.close()
    # return json.dumps(result_set)
    return jsonify(result_set)


@app.route('/registration', methods=('GET', 'POST'))
def registrarion():
    if request.method == 'POST':
        request_data = request.get_json()
        login = request_data['login']
        password = request_data['password']
        conn = get_db_connection()
        cur = conn.cursor()

# check if login exists
        cur.execute("SELECT login from main.USERS\
            WHERE login = '{0}';".format(login))
        result_check = cur.fetchall()
        if len(result_check) != 0:
            print("Login {0} is exists".format(login))
            return "Login {0} is exists".format(login)

# check if the login meets the requirements
        if len(password) < 5 or len(password) > 15 or " " in password:
            print("Password does not match requirements is exists")
            return "Password does not match requirements is exists"

        cur.execute('INSERT INTO main.USERS (login, password)'
                    'VALUES (%s, %s)',
                    (request_data['login'], request_data['password'])
                    )
        conn.commit()
        cur.close()
        conn.close()
    return jsonify(request_data)

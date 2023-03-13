import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

def get_database_connection():
    connection = psycopg2.connect(
        host = "localhost",
        database = "setbox",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD']
    )
    return connection

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/user')
def user():
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT subjects.name, lesson.date, lesson.progress FROM users JOIN subjects ON users.id = subjects.user_id JOIN lesson ON subjects.id = lesson.subject_id WHERE users.id = 1')
    subject_data = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('user.html', subject_data=subject_data)

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
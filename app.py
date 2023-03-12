from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

if __name__ == '__main__':
    app.run()
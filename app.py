from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/subject')
def subjects():
    return render_template('subjects_page.html')

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
from flask import Blueprint, render_template, request, send_file, make_response, redirect, url_for
from app.extensions.database.crud import Session
from app.extensions.database.models import Subject, Lesson, File
from datetime import datetime
from werkzeug.utils import secure_filename
from flask_login import login_required

blueprint = Blueprint('lesson', __name__)
@blueprint.route('/lesson/<lesson_id>')
@login_required
def lesson(lesson_id):
    s = Session()
    data_query=s.query(Lesson, Subject).filter(Subject.id == Lesson.subject_id).filter(Lesson.id == lesson_id).first()
    files=s.query(File).filter(File.lesson_id == Lesson.id).filter(Lesson.id == lesson_id).all()
    s.close()
    return render_template('lesson/lesson.html', info=data_query, files=files)

@blueprint.route('/upload/<lesson_id>', methods=['POST'])
@login_required
def upload(lesson_id):
    s = Session()
    file = request.files['file']
    name = request.form['name']
    filename = str(lesson_id) + "_" + datetime.now().strftime('%Y%m%d%H%M%S') + "_" + secure_filename(file.filename)
    file.save("./files/" + filename)
    file_to_db = File(
        filename = filename,
        name = name,
        lesson_id = lesson_id
    )
    s.add(file_to_db)
    s.commit()
    s.close()
    return redirect(url_for('lesson.lesson', lesson_id=lesson_id))

@blueprint.route('/files/<filename>', methods=['GET'])
@login_required
def download(filename):
    file_path = "../files/"+filename
    response = make_response(send_file(file_path))
    return response
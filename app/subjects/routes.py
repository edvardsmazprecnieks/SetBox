from flask import Blueprint, render_template, redirect, url_for
from app.extensions.database.crud import Session
from app.extensions.database.models import Subject, User, Lesson
from sqlalchemy import func
from flask_login import login_required, current_user

blueprint = Blueprint('subjects', __name__)


@blueprint.route('/subject')
@login_required
def subjects():
    s = Session()
    data = s.query(Subject).filter(User.id == Subject.owner_user_id).filter(Subject.owner_user_id == current_user.id).all()
    s.close()
    return render_template('subjects/subjects_page.html', subject_names=data)


@blueprint.route('/subject/<subject_id>')
@login_required
def subject(subject_id):
    s = Session()
    if current_user.id == s.query(Subject.owner_user_id).filter(Subject.id == subject_id).first()[0]:
        subject_name = s.query(Subject.name).filter(Subject.id == subject_id).first()
        data_query=s.query(Lesson).filter(Subject.id == Lesson.subject_id).filter(Subject.id == subject_id).order_by(Lesson.date.desc()).all()
        progress_test=s.query(func.avg(Lesson.progress).label('progress')).filter(Subject.id == Lesson.subject_id).filter(Subject.id == subject_id).first()
        s.close()
        return render_template('subjects/subject.html', subject_name=subject_name, subject_info=data_query, progress=progress_test.progress)
    else:
        return redirect(url_for('subjects.subjects'))


@blueprint.route('/subjectcreator')
def addlesson():
    return render_template('subjects/subjectcreator.html')


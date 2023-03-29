from flask import Blueprint, render_template
from app.extensions.database.crud import Session
from app.extensions.database.models import Subject, User, Lesson
from sqlalchemy import func

blueprint = Blueprint('subjects', __name__)

@blueprint.route('/')
@blueprint.route('/subject')
def subjects():
    s = Session()
    data = s.query(Subject).filter(User.id == Subject.owner_user_id).filter(Subject.owner_user_id == 1).all()
    s.close()
    return render_template('subjects/subjects_page.html', subject_names=data)


@blueprint.route('/subject/<subject_id>')
def subject(subject_id):
    s = Session()
    subject_name = s.query(Subject.name).filter(Subject.id == subject_id).first()
    data_query=s.query(Lesson).filter(Subject.id == Lesson.subject_id).filter(Subject.id == subject_id).order_by(Lesson.date.desc()).all()
    progress_test=s.query(func.avg(Lesson.progress).label('progress')).filter(Subject.id == Lesson.subject_id).filter(Subject.id == subject_id).first()
    s.close()
    return render_template('subjects/subject.html', subject_name=subject_name, subject_info=data_query, progress=progress_test.progress)


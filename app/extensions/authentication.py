from flask_login import LoginManager
from app.extensions.database.models import User
from app.extensions.database.crud import Session

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
  s = Session()
  user_id = s.query(User).get(user_id)
  s.close()
  return user_id
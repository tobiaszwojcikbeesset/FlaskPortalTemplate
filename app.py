from flask import Flask
from sys import argv
from extensions import db, login_manager
from common_functions import salt
from models.users import User, UserRole, Role, Address
# from translation import Translationa
import config


app = Flask(__name__)
app.config.from_object(config)
login_manager.init_app(app)

login_manager.login_view = 'user.login_page'

def trans(fraze):
    return fraze

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

db.init_app(app)

if "init" in argv:
    with app.app_context():
        db.create_all()
        role_list = []
        if int(Role.query.count()) == 0:
            roles = [['Admin','admin'],['Super admin','super_admin'],['Użytkownik','user']]
            
            for role in roles:
                new_role = Role(role[0],role[1])
                role_list.append(new_role)
                db.session.add(new_role)
        if int(User.query.count()) == 0:
            if len(role_list) == 0:
                role_list = Role.query.all()
                print(role_list)
            from werkzeug.security import generate_password_hash
            password =  generate_password_hash(salt(config.ADMIN_INITIAL_PASSWORD), method='pbkdf2:sha256')
            superAdmin = User('super_admin', config.MAIN_EMAIL, password)
            superAdmin.roles=role_list
            db.session.add(superAdmin)
        db.session.commit()




from blueprints.main import main_bp
app.register_blueprint(main_bp)

from blueprints.user import user_bp
app.register_blueprint(user_bp)


if __name__ == '__main__':
    
    app.run()
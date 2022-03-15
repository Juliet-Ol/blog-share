# from app import create_app,db
from app.models import User
from app import db
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand


from app.views import app


# Creating app instance
# app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, User=User)

if __name__ == '__main__':
    manager.run()



from app import app
from app.models import User
from app import db
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand


# from app.views import app


# Creating app instance
# app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, User=User, db=db)

if __name__ == '__main__':
    manager.run()



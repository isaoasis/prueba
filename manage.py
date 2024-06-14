from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from myblog import app, db

# Inicializa Flask-Migrate
migrate = Migrate(app, db)
manager = Manager(app)

# Añadir el comando de migración al manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

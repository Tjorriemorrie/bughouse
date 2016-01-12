#!flask/bin/python
from app import app, db

# migrations
from flask.ext.migrate import Migrate, MigrateCommand
migrate = Migrate(app, db)

# create manager
from flask.ext.script import Manager
manager = Manager(app)
manager.add_command('db', MigrateCommand)

manager.run()

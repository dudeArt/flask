# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'sukapzdcnaxas'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') #это путь к нашей бд
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository') # это папка, где мы будем хранить миграции


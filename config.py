import os

class Config:
    DEBUG = True
    TESTING = True

    # Configuración de base de datos 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgres://default:NjXqClpM73Kx@ep-curly-dawn-a4hwnczb-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require')

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    SECRET_KEY = 'dev'
    DEBUG = True
    TESTING = True

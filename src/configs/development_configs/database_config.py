import os


class MySQLConfig:
    MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')

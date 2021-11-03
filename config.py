"""Flask configuration."""

from os import environ

class MySQLConfig:
  MYSQL_DATABASE_HOST=environ.get("MYSQL_SERVICE_HOST")
  MYSQL_DATABASE_PORT=environ.get("MYSQL_SERVICE_PORT")
  MYSQL_DATABASE_USER="brucewayne"
  MYSQL_DATABASE_PASSWORD="batman"
  MYSQL_DATABASE_DB="superhero"

class Config(MySQLConfig):
  SECRET_KEY="dev"

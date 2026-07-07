from app.config import get_settings
import mysql.connector

settings = get_settings()


# MYSQL CONNECTION
db = mysql.connector.connect(
    host=settings.MYSQL_HOST,
    user=settings.MYSQL_USERNAME,
    password=settings.MYSQL_PASSWORD,
    database=settings.MYSQL_DATABASE,
    port=settings.MYSQL_PORT
)

from __init__ import *

# API Settings
app = Flask(__name__)
app.config["DEBUG"] = True

# Connection Settings
con = PostgreSQL(
    host='localhost',
    database='api',
    user='admin',
    password='admin',
)

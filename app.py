from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    conn = psycopg2.connect("postgresql://example_flask_postgres_user:TuGDkrG6vTY4EEvhzlz6AX5ZAmI85BtD@dpg-d47gkm24d50c7385kbk0-a/example_flask_postgres")
    conn.close()
    return 'Hello World! from Adam Horn in 3308'

@app.route("/db_test")
def testing():
    conn = psycopg2.connect("postgresql://example_flask_postgres_user:TuGDkrG6vTY4EEvhzlz6AX5ZAmI85BtD@dpg-d47gkm24d50c7385kbk0-a/example_flask_postgres")
    conn.close()
    return "Database Connection Successful"
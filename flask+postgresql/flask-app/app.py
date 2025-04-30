from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        dbname=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
        host=os.environ.get("DB_HOST"),
        port="5432"
    )

@app.route("/")
def home():
    try:
        conn = get_db_connection()
        conn.close()
        db_status = "PostgreSQL connection successful!"
    except Exception as e:
        db_status = f"Database connection failed: {e}"

    return render_template("home.html", db_status=db_status)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

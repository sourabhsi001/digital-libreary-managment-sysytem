from flask import Flask
from config import Config
from models import db
app=Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
@app.route("/")
def home():
    return"SITE ON WORKING "

with app.app_context():
    try:
        db.engine.connect()
        print("✅ Database Connected Successfully!")
    except Exception as e:
        print("❌ Database Connection Failed!")
        print(e)

if __name__=="__main__":
    
    app.run(debug=True)
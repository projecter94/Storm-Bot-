from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "H-zz-H C2 is Online - Keep Alive Active"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=False)

def keep_alive():
    t = Thread(target=run, daemon=True)
    t.start()
    print("[Keep-Alive] Flask server started successfully")
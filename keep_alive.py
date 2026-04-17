from flask import Flask
from threading import Thread
import os
import time

app = Flask('')

@app.route('/')
def home():
    return "H-zz-H C2 Online - Keep Alive Active"

def run():
    port = int(os.environ.get("PORT", 8080))
    print(f"[Keep-Alive] Flask server starting on 0.0.0.0:{port}")
    app.run(host='0.0.0.0', port=port, debug=False)

def keep_alive():
    t = Thread(target=run, daemon=True)
    t.start()
    print("[Keep-Alive] Thread started successfully")
    time.sleep(3)  # Give Render time to detect the port

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
  port = os.environ.get('PORT', 'unknown')
  return f"Hello! This response is from port {port}.\n"

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
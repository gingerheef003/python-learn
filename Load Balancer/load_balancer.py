from flask import Flask
import requests

app = Flask(__name__)

BACKENDS = ["http://127.0.0.1:5000", "http://127.0.0.1:5001", "http://127.0.0.1:5002"]
current_backend = 0

@app.route('/')
def load_balance():
  global current_backend
  backend = BACKENDS[current_backend]

  try:
    response = requests.get(backend)
    current_backend = (current_backend + 1) % len(BACKENDS)
    return response.text
  except requests.exceptions.RequestException:
    return f"Backend {backend} is down!", 500

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3000)

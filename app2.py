from flask import Flask, request
import requests

app = Flask(__name__)

# Replace this with the URL you want to forward requests to
TARGET_URL = "http://192.168.0.11:8080/github-webhook/"

@app.route('/', methods=['POST'])
def proxy():
    # Forward the incoming request to the target URL
    response = requests.post(
        TARGET_URL,
        data=request.data,
        headers=request.headers
    )

    # Return the response from the target server
    return response.content, response.status_code, response.headers.items()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
